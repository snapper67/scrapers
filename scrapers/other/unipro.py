import json
import re
from typing import Dict, List, Optional

import requests
from bs4 import BeautifulSoup

class UniProScraper:
    """Scraper for UniPro Foodservice distributor directory."""
    MARKETS = [
  {"market": "New York City, NY", "zipcode": "10001"},
  {"market": "Los Angeles, CA", "zipcode": "90001"},
  {"market": "Chicago, IL", "zipcode": "60601"},
  {"market": "Houston, TX", "zipcode": "77002"},
  {"market": "Dallas-Fort Worth, TX", "zipcode": "75201"},
  {"market": "Miami, FL", "zipcode": "33101"},
  {"market": "Atlanta, GA", "zipcode": "30303"},
  {"market": "Philadelphia, PA", "zipcode": "19102"},
  {"market": "Washington, DC", "zipcode": "20001"},
  {"market": "Phoenix, AZ", "zipcode": "85001"},
  {"market": "Boston, MA", "zipcode": "02108"},
  {"market": "Seattle, WA", "zipcode": "98101"},
  {"market": "Detroit, MI", "zipcode": "48226"},
  {"market": "San Diego, CA", "zipcode": "92101"},
  {"market": "San Francisco, CA", "zipcode": "94102"},
  {"market": "Tampa, FL", "zipcode": "33602"},
  {"market": "Minneapolis, MN", "zipcode": "55401"},
  {"market": "Las Vegas, NV", "zipcode": "89101"},
  {"market": "Denver, CO", "zipcode": "80202"},
  {"market": "Riverside-San Bernardino, CA", "zipcode": "92501"},
  {"market": "San Antonio, TX", "zipcode": "78205"},
  {"market": "Baltimore, MD", "zipcode": "21201"},
  {"market": "Charlotte, NC", "zipcode": "28202"},
  {"market": "Austin, TX", "zipcode": "78701"},
  {"market": "Sacramento, CA", "zipcode": "95814"},
  {"market": "Portland, OR", "zipcode": "97201"},
  {"market": "St. Louis, MO", "zipcode": "63101"},
  {"market": "Orlando, FL", "zipcode": "32801"},
  {"market": "Indianapolis, IN", "zipcode": "46204"},
  {"market": "San Jose, CA", "zipcode": "95113"},
  {"market": "Cincinnati, OH", "zipcode": "45202"},
  {"market": "Cleveland, OH", "zipcode": "44114"},
  {"market": "Kansas City, MO", "zipcode": "64106"},
  {"market": "Columbus, OH", "zipcode": "43215"},
  {"market": "Pittsburgh, PA", "zipcode": "15222"},
  {"market": "Raleigh, NC", "zipcode": "27601"},
  {"market": "Virginia Beach, VA", "zipcode": "23451"},
  {"market": "Milwaukee, WI", "zipcode": "53202"},
  {"market": "Jacksonville, FL", "zipcode": "32202"},
  {"market": "Nashville, TN", "zipcode": "37219"},
  {"market": "Salt Lake City, UT", "zipcode": "84101"},
  {"market": "Providence, RI", "zipcode": "02903"},
  {"market": "Memphis, TN", "zipcode": "38103"},
  {"market": "Richmond, VA", "zipcode": "23219"},
  {"market": "Louisville, KY", "zipcode": "40202"},
  {"market": "McAllen, TX", "zipcode": "78501"},
  {"market": "Oklahoma City, OK", "zipcode": "73102"},
  {"market": "Tucson, AZ", "zipcode": "85701"},
  {"market": "Hartford, CT", "zipcode": "06103"},
  {"market": "New Orleans, LA", "zipcode": "70112"}
]


    def __init__(self):
        self.base_url = "https://www.uniprofoodservice.com"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        })

    def get_distributor_details(self, branch_id: int) -> Optional[Dict]:
        """
        Get detailed information for a specific distributor.
        
        Args:
            branch_id: The branch ID of the distributor
            
        Returns:
            Dictionary containing detailed distributor information or None if not found
        """
        try:
            url = f"{self.base_url}/distributors/directory/{branch_id}"
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            # Parse the JSON response
            return response.json()
            
        except Exception as e:
            print(f"Error fetching details for branch {branch_id}: {str(e)}")
            return None
    
    def get_distributors(self, zip_code: str, radius: int = 1000, distributor_type: str = "Broadline Foodservice") -> List[Dict]:
        """
        Get a list of distributors from UniPro Foodservice directory.
        
        Args:
            zip_code: Zip code to search near
            radius: Search radius in miles (default: 1000)
            distributor_type: Type of distributor to search for (default: "Broadline Foodservice")
            
        Returns:
            List of dictionaries containing distributor information
        """
        params = {
            'distributorType': distributor_type,
            'radius': radius,
            'search': zip_code
        }

        print(params)
        
        try:
            response = self.session.get(
                f"{self.base_url}/distributors/directory",
                params=params,
                timeout=30
            )
            response.raise_for_status()
            
            # Parse the page to extract the JSON data
            soup = BeautifulSoup(response.text, 'html.parser')
            app_div = soup.find('div', {'id': 'app'})
            
            if not app_div or 'data-page' not in app_div.attrs:
                print("Could not find data-page attribute in the response")
                return []
                
            # Parse the JSON data
            page_data = json.loads(app_div['data-page'])
            distributors = page_data.get('props', {}).get('distributors', {})
            
            # Convert to list of dictionaries and fetch details for each
            result = []
            for dist_id, dist_data in distributors.items():
                distributor = {
                    'branch_id': dist_data.get('branch_id'),
                    'name': dist_data.get('branch_name', '').strip(),
                    'city': dist_data.get('city', '').strip(),
                    'state': dist_data.get('state', '').strip(),
                    'type': dist_data.get('distributor_type', '').strip(),
                    'distance': dist_data.get('geo_distance', '').strip(),
                    'details': None,
                    'market': ''
                }
                
                # Fetch additional details if branch_id is available
                if distributor['branch_id']:
                    distributor['details'] = self.get_distributor_details(distributor['branch_id'])
                
                result.append(distributor)
                
            return result
            
        except Exception as e:
            print(f"Error fetching distributors: {str(e)}")
            return []


def main():
    """Example usage of the UniProScraper."""
    scraper = UniProScraper()
    zip_code = "23236"  # Example zip code
    distributors = scraper.get_distributors(zip_code)

    print(f"Found {len(distributors)} distributors near {zip_code}:")
    for i, dist in enumerate(distributors, 1):
        print(f"{i}. {dist['name']} - {dist['city']}, {dist['state']} ({dist['distance']})")


if __name__ == "__main__":
    main()
