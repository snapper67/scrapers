import csv
import glob
import os
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path
from typing import Dict, List, Tuple, Union


class CSVProcessor:
	"""
	A utility class for processing CSV files with various operations.
	"""

	@staticmethod
	def remove_duplicates(input_file, output_file=None, column='sku'):
		"""
		Remove duplicate rows from a CSV file based on the SKU column.

		Args:
			input_file (str): Path to the input CSV file
			output_file (str, optional): Path to save the deduplicated CSV.
									   If None, will append '_deduped' to input filename.

		Returns:
			str: Path to the output file with duplicates removed
		"""
		if output_file is None:
			base, ext = os.path.splitext(input_file)
			output_file = f"{base}_deduped{ext}"

		# Read the input file
		try:
			df = pd.read_csv(input_file, dtype=str, keep_default_na=False)
		except Exception as e:
			print(f"Error reading input file: {e}")
			return None

		# Check if 'sku' column exists
		if column not in df.columns:
			print("Error: 'sku' column not found in the input file")
			return None

		# Remove duplicates based on 'sku' column
		initial_count = len(df)
		df_deduped = df.drop_duplicates(subset=[column], keep='first')
		final_count = len(df_deduped)

		# Save the deduplicated data
		try:
			df_deduped.to_csv(output_file, index=False)
			print(f"Removed {initial_count - final_count} duplicate SKUs. "
			      f"Saved {final_count} unique SKUs to {output_file}")
			return output_file
		except Exception as e:
			print(f"Error writing output file: {e}")
			return None

	@staticmethod
	def count_rows_in_data_csvs(directory: str) -> Dict[str, Dict]:
		"""
		Count rows in all CSV files containing 'data' or 'urls' in their filenames across all subdirectories.

		Args:
			directory (str): Root directory to search for CSV files

		Returns:
			Dict[str, Dict]: A dictionary where keys are subdirectory paths and values are
				dictionaries with:
				- 'files': list of dicts with file info and row counts
				- 'total_rows': total rows across all files
				- 'url_rows': total rows in URL files
				- 'data_rows': total rows in data files
		"""
		print(f"Scanning directory: {directory}")
		results = {}

		try:
			# First, check if there are any subdirectories
			subdirs = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

			if not subdirs:
				# If no subdirectories, use the base directory
				dirs_to_scan = [directory]
				use_base_dir = True
			else:
				# Otherwise, scan all subdirectories
				dirs_to_scan = [os.path.join(directory, d) for d in subdirs]
				use_base_dir = False

			for dir_path in dirs_to_scan:
				# If we're using the base directory, use its name as the key
				if use_base_dir:
					dir_key = os.path.basename(os.path.normpath(directory))
				else:
					dir_key = os.path.basename(dir_path)

				if dir_key not in results:
					results[dir_key] = {
						'files': {},
						'total_rows': 0,
						'url_rows': 0,
						'data_rows': 0
					}

				for root, _, files in os.walk(dir_path):
					for file in files:
						if not file.endswith('.csv'):
							continue

						if 'data' not in file.lower() and 'url' not in file.lower():
							continue

						csv_file = os.path.join(root, file)
						try:
							with open(csv_file, 'r', encoding='utf-8') as f:
								row_count = sum(1 for row in csv.reader(f)) - 1
							print(f"Found {row_count} rows in {csv_file}")
							# print(row_count)
							file_entry = {
								'file_name': file,
								'file_path': csv_file,
								'row_count': row_count,
								'type': 'data' if 'data' in file.lower() else 'urls'
							}

							results[dir_key]['files'][file] = file_entry
							results[dir_key]['total_rows'] += row_count

							if 'url' in file.lower():
								results[dir_key]['url_rows'] += row_count
							else:
								results[dir_key]['data_rows'] += row_count

							print(f"Found {row_count} rows in {csv_file}")

						except Exception as e:
							print(f"Error processing {csv_file}: {e}")
							continue

		except Exception as e:
			print(f"Error scanning directory {directory}: {e}")

		# Convert the files dictionary to a list for the final output
		for dir_data in results.values():
			dir_data['files'] = list(dir_data['files'].values())

		return results

	def html_table_to_csv(html_content, output_file='products_export.csv'):
		"""
		Convert an HTML table to a CSV file.

		Args:
			html_content (str): HTML content containing a table
			output_file (str): Path to save the CSV file

		Returns:
			str: Path to the output CSV file if successful, None otherwise
		"""
		try:
			# Parse the HTML content
			soup = BeautifulSoup(html_content, 'html.parser')

			# Find the table
			table = soup.find('table')
			if not table:
				print("No table found in the HTML content")
				return None

			# Extract table headers
			headers = []
			header_row = table.find('thead').find('tr') if table.find('thead') else table.find('tr')
			for th in header_row.find_all(['th', 'td']):
				headers.append(th.get_text(strip=True))

			# Extract table data
			rows = []
			for row in table.find_all('tr')[1:]:  # Skip header row
				cells = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
				rows.append(cells)

			# Write to CSV
			with open(output_file, 'w', newline='', encoding='utf-8') as f:
				writer = csv.writer(f)
				writer.writerow(headers)
				writer.writerows(rows)

			print(f"Successfully converted HTML table to {output_file}")
			return output_file

		except Exception as e:
			print(f"Error converting HTML table to CSV: {e}")
			return None

	@staticmethod
	def count_csv_rows(directory='.'):
		"""
		Counts the number of rows in all CSV files in the specified directory.

		Args:
			directory (str): Path to the directory containing CSV files. Defaults to current directory.

		Returns:
			str: Formatted string with the results
		"""
		try:
			# Find all CSV files in the directory
			csv_files = glob.glob(os.path.join(directory, '*.csv'))

			if not csv_files:
				return "No CSV files found in the specified directory."

			results = []
			total_rows = 0

			# Count rows in each CSV file
			for file_path in csv_files:
				try:
					with open(file_path, 'r', encoding='utf-8') as f:
						row_count = sum(1 for row in f) - 1  # Subtract 1 for header
					total_rows += row_count
					results.append(f"{os.path.basename(file_path)}: {row_count} rows")
				except Exception as e:
					results.append(f"Error processing {os.path.basename(file_path)}: {str(e)}")

			# Add total count
			results.append(f"\nTotal rows across all CSV files: {total_rows}")

			return "\n".join(results)

		except Exception as e:
			return f"Error counting CSV rows: {str(e)}"

	@staticmethod
	def combine_three_csvs(file1, file2, file3, output_file=None):
		"""
		Combine three CSV files into one after verifying they have the same columns.

		Args:
			file1 (str): Path to the first CSV file
			file2 (str): Path to the second CSV file
			file3 (str): Path to the third CSV file
			output_file (str, optional): Path to save the combined CSV.
							   If None, will use 'combined_output.csv' in the current directory.

		Returns:
			str: Path to the output file

		Raises:
			ValueError: If the input files don't have the same columns
		"""
		if output_file is None:
			output_file = 'combined_output.csv'

		# Read all three dataframes
		df1 = pd.read_csv(file1)
		df2 = pd.read_csv(file2)
		df3 = pd.read_csv(file3)

		# Get column sets for comparison
		cols1 = set(df1.columns)
		cols2 = set(df2.columns)
		cols3 = set(df3.columns)

		# Check if all column sets are equal
		if not (cols1 == cols2 == cols3):
			raise ValueError("Input files must have the same columns")

		# Combine the dataframes
		combined_df = pd.concat([df1, df2, df3], ignore_index=True)

		# Save the combined dataframe
		combined_df.to_csv(output_file, index=False)
		return output_file

	@staticmethod
	def reorder_columns_to_match(source_file, reference_file, output_file=None):
		"""
		Reorder columns in the source CSV file to match the column order in the reference CSV file.

		Args:
			source_file (str): Path to the CSV file whose columns need reordering
			reference_file (str): Path to the CSV file with the desired column order
			output_file (str, optional): Path to save the reordered CSV.
						   If None, will append '_reordered' to source filename.

		Returns:
			str: Path to the output file with reordered columns

		Raises:
			ValueError: If the files don't have the same set of columns
		"""
		if output_file is None:
			base, ext = os.path.splitext(source_file)
			output_file = f"{base}_reordered{ext}"

		# Read both CSV files
		source_df = pd.read_csv(source_file)
		reference_df = pd.read_csv(reference_file)

		# Get column sets
		source_cols = set(source_df.columns)
		reference_cols = set(reference_df.columns)

		# Check if both files have the same columns
		if source_cols != reference_cols:
			missing_in_source = reference_cols - source_cols
			extra_in_source = source_cols - reference_cols
			error_msg = []
			if missing_in_source:
				error_msg.append(f"Columns in reference but not in source: {', '.join(missing_in_source)}")
			if extra_in_source:
				error_msg.append(f"Columns in source but not in reference: {', '.join(extra_in_source)}")
			raise ValueError("\n".join(error_msg))

		# Reorder columns in source to match reference order
		reordered_df = source_df[reference_df.columns]

		# Save the reordered dataframe
		reordered_df.to_csv(output_file, index=False)
		return output_file

	@staticmethod
	def update_distributor_in_csvs(directory: str, distributor_name: str) -> dict:
		"""
		Update or add distributor_name column in all CSV files in the specified directory.

		Args:
			directory (str): Directory containing CSV files to update
			distributor_name (str): Distributor name to set in the distributor_name column

		Returns:
			dict: Dictionary containing results of the operation
		"""
		if not os.path.isdir(directory):
			return {
				'success': False,
				'message': f"Error: '{directory}' is not a valid directory."
			}

		csv_files = list(Path(directory).rglob('*data*.csv'))

		if not csv_files:
			return {
				'success': False,
				'message': f"No CSV files found in directory: {directory}"
			}

		results = {
			'total_files': len(csv_files),
			'files_updated': 0,
			'files_skipped': 0,
			'errors': [],
			'updated_files': []
		}

		for csv_file in csv_files:
			try:
				# Read the CSV file
				df = pd.read_csv(csv_file, dtype=str, keep_default_na=False)

				# Add or update distributor_name column
				df['distributor_name'] = distributor_name

				# Save the updated CSV
				df.to_csv(csv_file, index=False)

				results['files_updated'] += 1
				results['updated_files'].append(str(csv_file.relative_to(directory)))

			except Exception as e:
				error_msg = f"Error processing {csv_file.name}: {str(e)}"
				results['errors'].append(error_msg)
				results['files_skipped'] += 1
				continue

		results['success'] = results['files_updated'] > 0
		if results['files_updated'] == results['total_files']:
			results['message'] = f"Successfully updated distributor name in all {results['files_updated']} CSV files."
		else:
			results['message'] = (
				f"Updated {results['files_updated']} out of {results['total_files']} files. "
				f"Skipped {results['files_skipped']} files due to errors."
			)

		return results

	def add_distributor_name(self, *args, **options):
		directory = options['directory']
		distributor_name = options['distributor_name']

		if not os.path.isdir(directory):
			return f"Error: '{directory}' is not a valid directory."

		csv_files = glob.glob(os.path.join(directory, "**/*.csv"), recursive=True)

		if not csv_files:
			return "No CSV files found in the directory."

		for file_name in csv_files:
			file_path = os.path.join(directory, file_name)
			try:
				df = pd.read_csv(file_path)

				if 'distributor_name' not in df.columns:
					self.stdout.write(self.style.WARNING(f"Skipped '{file_name}': No 'distributor_name' column."))
					continue

				df['distributor_name'] = distributor_name
				df.to_csv(file_path, index=False)
				return f"Updated '{file_name}' successfully."

			except Exception as e:
				return f"Failed to update '{file_name}': {str(e)}"
		return "CSV Files Updated."

	import os
	import csv
	from typing import List, Dict, Optional

	def find_skus_starting_with_zero(directory: str, column: str) -> Dict[str, List[Dict]]:
		"""
		Scans all CSV files in the specified directory and checks for SKUs that start with zero.

		Args:
			directory (str): Path to the directory containing CSV files to scan

		Returns:
			Dict[str, List[Dict]]: Dictionary with filenames as keys and lists of rows with SKUs starting with zero
		"""
		results = {}

		# Check if directory exists
		if not os.path.isdir(directory):
			raise NotADirectoryError(f"The directory {directory} does not exist")

		# Iterate through all files in the directory
		for filename in os.listdir(directory):
			if not filename.lower().endswith('.csv'):
				continue

			filepath = os.path.join(directory, filename)
			rows_with_zero_skus = []

			try:
				with open(filepath, 'r', encoding='utf-8', newline='') as csvfile:
					reader = csv.DictReader(csvfile)

					# Check if 'Sku' column exists
					if 'Sku' not in reader.fieldnames:
						continue

					# Scan each row
					for row_num, row in enumerate(reader, 2):  # Start from 2 for 1-based line numbers
						value = row.get(column, '').strip()
						if value and value[0] == '0':
							rows_with_zero_skus.append({
								'row_number': row_num,
								column : value,
								'row_data': row
							})

				# Add to results if we found any matching SKUs
				if rows_with_zero_skus:
					results[filename] = rows_with_zero_skus

			except Exception as e:
				print(f"Error processing {filename}: {str(e)}")
				continue

		return results