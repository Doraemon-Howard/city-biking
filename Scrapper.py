import re
import requests
from bs4 import BeautifulSoup

def scrape_all_city_ratings():
    url = "https://cityratings.peopleforbikes.org/ratings"
    headers = {"User-Agent": "Mozilla/5.0 (Data Collection Script)"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    # Select all data rows. Based on the provided code, data rows have class "sc-b1308c1e-3 fJTaOc"
    rows = soup.select('tr.sc-b1308c1e-3.fJTaOc')

    city_data = []
    for row in rows:
        tds = row.find_all('td', class_='sc-b1308c1e-4 cmWJdr')
        if len(tds) < 4:
            # In case of unexpected row format
            continue

        city_link = tds[0].find('a')
        city_name = city_link.get_text(strip=True) if city_link else tds[0].get_text(strip=True)
        score = tds[3].get_text(strip=True)  # 4th column is the score

        city_data.append({
            'city': city_name,
            'rating': score
        })
    return city_data

def normalize_city_name(name):
    # Convert to lowercase
    name = name.lower()
    # Remove parentheses and their contents
    name = re.sub(r'\(.*?\)', '', name)
    # Strip quotes
    name = name.strip('\'"')
    # Trim after comma if present (e.g. "Philadelphia, PA" -> "Philadelphia")
    if ',' in name:
        parts = name.split(',', 1)
        # Take the first part which is presumably the city name
        name = parts[0]
    # Remove extra whitespace
    name = name.strip()
    return name

def find_bikeshare_service(user_city):
    api_url = "http://api.citybik.es/v2/networks"
    resp = requests.get(api_url)
    resp.raise_for_status()
    data = resp.json()

    # Normalize the user input city
    normalized_user_city = normalize_city_name(user_city)

    matches = []
    for network in data.get('networks', []):
        location = network.get('location', {})
        city_name = location.get('city', '')
        # Normalize API city name
        normalized_api_city = normalize_city_name(city_name)

        if normalized_api_city == normalized_user_city:
            matches.append(network['name'])

    return matches



if __name__ == "__main__":
    user_city = input("Enter a city name: ").strip()
    data = scrape_all_city_ratings()

    rating = None
    for entry in data:
        if entry['city'].lower() == user_city.lower():
            rating = entry['rating']
            break

    if rating:
        print(f"The biking rating for {user_city} is: {rating}")
    else:
        print("City Not Ranked")

    bikeshare_services = find_bikeshare_service(user_city)
    if bikeshare_services:
        print(f"Bikeshare services available in {user_city}:")
        for service in bikeshare_services:
            print("-", service)
    else:
        print(f"No bikeshare service found in {user_city}.")