**README.md**  
**Project Overview**

This project collects and consolidates two key types of bicycle-related data:

1. **Bike Ratings Data**:  
   Using a web scraper, we gather public city biking ratings from the [PeopleForBikes City Ratings](https://cityratings.peopleforbikes.org/ratings) website. This data provides an “overall score” reflecting how bike-friendly various cities are. It measures factors like infrastructure quality, ridership levels, safety, and related metrics. We chose this site because:  
   * **Reputable Source**: PeopleForBikes is a well-known advocacy organization dedicated to making biking better for everyone.  
   * **Unique Data**: The site provides a specialized rating system not widely replicated elsewhere, offering a standardized measure of bike-friendliness across many North American cities.  
   * **Easy Web Access**: The ratings are publicly displayed online but not conveniently downloadable as a ready-to-use dataset.  
2. **Bikeshare Network Data**:  
   Through the [CityBikes API](http://api.citybik.es/v2/), we gather information about bikeshare networks available around the world, including city location and the companies operating these systems. The API is free and publicly available, making it an excellent choice to complement the bike rating data.

**Purpose**

**Why gather these datasets together?**

Cycling infrastructure quality (as represented by a city’s bike rating) and access to bikeshare services are crucial data points for planners, advocates, tourists, and citizens. Combining these:

* **Travel & Tourism**: A tourist can determine how easy and safe it is to get around a city by bike and which bikeshare service to use.  
* **Urban Planning & Advocacy**: City planners or advocates can identify gaps—cities with high bike ratings but no bikeshare systems, or those with bikeshare but lower ratings where improvements could encourage more ridership.  
* **Commuters & Residents**: Local commuters can see if their city is improving over time, and what bikeshare options might exist for their daily travels.

**Why is such a dataset not readily available for free?**

* **Fragmented Data Sources**: Bike ratings are maintained by advocacy organizations and are not typically integrated with open bikeshare service listings.  
* **Lack of Standardization**: Different data providers (PeopleForBikes and CityBikes) focus on unique aspects of the cycling ecosystem. Merging these viewpoints is non-trivial.  
* **Data Access Effort**: While both data sources are public, extracting, normalizing, and merging them into a cohesive dataset require time, technical skill, and careful handling. Many organizations or individuals may not have the resources or motivation to produce such a compiled dataset for free distribution.

By offering both datasets in a combined format, we provide valuable, actionable insights that are not currently packaged together elsewhere, making it easier for stakeholders to leverage this information.

**How to Run**

**Prerequisites**:

* Python 3.7+  
* Git (to clone the repository)

**Setup Steps**:

**Clone the Repository**:  
`git clone https://github.com/your-username/your-repo-name.git`  
`cd your-repo-name`

1. 

**Install Dependencies**:  
Ensure you have `pip` installed. Then:  
`pip install -r requirements.txt`

2. This installs `requests`, `beautifulsoup4`, and any other required packages.

**Run the Script**:  
`python city_bike_ratings.py`

3.   
4. **Interaction**:  
   The script will prompt you for a city name. After you enter a city (e.g., “Philadelphia”), it will:  
   * Display that city’s PeopleForBikes biking rating (if found).  
   * Display any bikeshare networks available in that city via the CityBikes API.

**Output**:

You’ll see console output similar to:

`Enter a city name: Philadelphia`  
`The biking rating for Philadelphia is: 71`  
`Bikeshare services available in Philadelphia:`  
`- Indego`

If a city’s rating or bikeshare services are not found, the script will inform you accordingly.

