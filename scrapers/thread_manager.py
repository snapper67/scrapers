import threading
import uuid
from typing import Dict, Optional, Callable, Any
from django.core.cache import cache


class ThreadManager:
    """
    A thread manager to handle background tasks with the ability to stop them gracefully.
    """
    _instance = None
    _threads: Dict[str, threading.Thread] = {}
    _stop_events: Dict[str, threading.Event] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ThreadManager, cls).__new__(cls)
        return cls._instance

    def start_thread(
        self,
        target: Callable,
        args: tuple = None,
        kwargs: Dict[str, Any] = None,
        task_id: str = None,
        timeout: int = 3600
    ) -> str:
        """
        Start a new thread and track it with the given task_id.
        
        Args:
            target: The target function to run in the thread
            args: Arguments to pass to the target function
            kwargs: Keyword arguments to pass to the target function
            task_id: Optional task ID (will generate one if not provided)
            timeout: Time in seconds before the thread is considered stale
            
        Returns:
            str: The task ID for the started thread
        """
        if args is None:
            args = ()
        if kwargs is None:
            kwargs = {}
            
        if task_id is None:
            task_id = str(uuid.uuid4())
            
        # Create a stop event for this thread
        stop_event = threading.Event()
        self._stop_events[task_id] = stop_event
        
        # Add the stop event to kwargs if the target function accepts it
        if 'stop_event' in target.__code__.co_varnames:
            kwargs['stop_event'] = stop_event
            
        # Create and start the thread
        thread = threading.Thread(
            target=self._thread_wrapper,
            args=(target, args, kwargs, task_id, stop_event),
            daemon=True
        )
        
        # Store the thread
        self._threads[task_id] = thread
        
        # Set initial progress in cache
        cache.set(
            f'product_processing_progress_{task_id}',
            {'status': 'started', 'message': 'Task started'},
            timeout=timeout
        )
        
        # Start the thread
        thread.start()
        
        # Store thread info in cache for potential restarts
        cache.set(
            f'thread_info_{task_id}',
            {'target': target.__name__, 'args': str(args), 'kwargs': str(kwargs)},
            timeout=timeout
        )
        
        return task_id
    
    def _thread_wrapper(self, target, args, kwargs, task_id, stop_event):
        """Wrapper function to handle thread execution and cleanup."""
        try:
            # Call the target function
            result = target(*args, **kwargs)
            
            # Update progress on successful completion
            progress = cache.get(f'product_processing_progress_{task_id}', {})
            if progress.get('status') != 'stopped':  # Don't overwrite 'stopped' status
                progress.update({
                    'status': 'completed',
                    'message': 'Task completed successfully',
                    'result': result
                })
                cache.set(f'product_processing_progress_{task_id}', progress, timeout=3600)
                
        except Exception as e:
            # Update progress on error
            progress = cache.get(f'product_processing_progress_{task_id}', {})
            progress.update({
                'status': 'error',
                'error': str(e),
                'message': f'Error in task: {str(e)}'
            })
            cache.set(f'product_processing_progress_{task_id}', progress, timeout=3600)
            
        finally:
            # Clean up
            self._cleanup_thread(task_id)
    
    def stop_thread(self, task_id: str) -> bool:
        """
        Immediately stop a thread and clean up its resources.
        
        Args:
            task_id: The ID of the task to stop
            
        Returns:
            bool: True if the thread was found and stopped, False otherwise
        """
        print(f'[DEBUG] Attempting to stop thread {task_id}')
        
        # Check if we have a valid thread to stop
        if task_id not in self._threads:
            print(f'[DEBUG] Thread {task_id} not found in active threads')
            return False
            
        thread = self._threads[task_id]
        
        # 1. Try to signal the thread to stop gracefully first
        if task_id in self._stop_events:
            print(f'[DEBUG] Setting stop event for thread {task_id}')
            self._stop_events[task_id].set()
            
            # Give it a very short time to respond to the stop event
            thread.join(timeout=0.1)
            
        # 2. Force stop if still alive
        if thread.is_alive():
            print(f'[DEBUG] Force stopping thread {task_id}')
            try:
                # This is a more forceful way to stop the thread
                import ctypes
                import sys
                
                if hasattr(thread, '_thread_id'):
                    thread_id = thread._thread_id
                else:
                    # Get thread ID for Python 3.8+
                    for tid, tobj in threading._active.items():
                        if tobj is thread:
                            thread_id = tid
                            break
                
                # Raise an exception in the thread to force it to stop
                res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
                    ctypes.c_long(thread_id),
                    ctypes.py_object(SystemExit)
                )
                
                if res == 0:
                    print(f'[DEBUG] Failed to raise exception in thread {task_id}')
                elif res != 1:
                    # If it returns a number greater than one, you're in trouble,
                    # and you should call it again with exc=NULL to revert the effect
                    ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), None)
                    print(f'[DEBUG] Failed to stop thread {task_id} cleanly')
                
            except Exception as e:
                print(f'[DEBUG] Error stopping thread: {e}')
        
        # 3. Clean up regardless of success
        self._cleanup_thread(task_id)
        
        # 4. Update progress to reflect the forced stop
        progress = cache.get(f'product_processing_progress_{task_id}', {})
        progress.update({
            'status': 'stopped',
            'message': 'Task was forcefully stopped',
            'force_stopped': True
        })
        cache.set(f'product_processing_progress_{task_id}', progress, timeout=3600)
        
        print(f'[DEBUG] Thread {task_id} stop completed')
        return True
    
    def _cleanup_thread(self, task_id: str):
        print(f'Cleaning up thread {task_id}')
        """Clean up resources for a thread."""
        if task_id in self._threads:
            thread = self._threads.pop(task_id)
            if thread.is_alive():
                thread.join(timeout=5)  # Wait up to 5 seconds for the thread to finish
                
        if task_id in self._stop_events:
            del self._stop_events[task_id]
    
    def get_thread_status(self, task_id: str) -> Optional[dict]:
        """
        Get the status of a thread.
        
        Args:
            task_id: The ID of the task to check
            
        Returns:
            Optional[dict]: The thread status or None if not found
        """
        if task_id in self._threads:
            thread = self._threads[task_id]
            return {
                'alive': thread.is_alive(),
                'name': thread.name,
                'daemon': thread.daemon
            }
        return None
    
    def get_all_threads(self) -> Dict[str, dict]:
        """Get information about all tracked threads."""
        return {
            task_id: {
                'alive': thread.is_alive(),
                'name': thread.name,
                'daemon': thread.daemon
            }
            for task_id, thread in self._threads.items()
        }


# Global thread manager instance
thread_manager = ThreadManager()


def start_background_task(
    target: Callable,
    args: tuple = None,
    kwargs: Dict[str, Any] = None,
    task_id: str = None,
    timeout: int = 3600
) -> str:
    """
    Start a background task using the global thread manager.
    
    Args:
        target: The target function to run in the thread
        args: Arguments to pass to the target function
        kwargs: Keyword arguments to pass to the target function
        task_id: Optional task ID (will generate one if not provided)
        timeout: Time in seconds before the thread is considered stale
        
    Returns:
        str: The task ID for the started thread
    """
    return thread_manager.start_thread(target, args, kwargs, task_id, timeout)


def stop_background_task(task_id: str) -> bool:
    """
    Stop a background task.
    
    Args:
        task_id: The ID of the task to stop
        
    Returns:
        bool: True if the task was found and stopped, False otherwise
    """
    return thread_manager.stop_thread(task_id)


def get_task_status(task_id: str) -> Optional[dict]:
    """
    Get the status of a background task.
    
    Args:
        task_id: The ID of the task to check
        
    Returns:
        Optional[dict]: The task status or None if not found
    """
    return thread_manager.get_thread_status(task_id)
