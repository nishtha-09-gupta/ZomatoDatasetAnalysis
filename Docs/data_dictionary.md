# Data Dictionary

## Dataset Overview

This dataset contains information about restaurants listed on Zomato. It includes details related to ratings, pricing, services like online ordering and table booking, as well as location and category information. The data has been cleaned and processed to make it suitable for analysis and visualization.


## Column Details

### 1. name

* **Type:** String
* **Description:** Name of the restaurant
* **Usage:** Used for identifying and counting unique restaurants


### 2. online_order

* **Type:** Integer (0/1)
* **Description:** Indicates whether online ordering is available

  * 1 = Yes
  * 0 = No
* **Usage:** Helps compare restaurants based on online service availability



### 3. book_table

* **Type:** Integer (0/1)
* **Description:** Indicates whether table booking is available

  * 1 = Yes
  * 0 = No
* **Usage:** Useful for analyzing premium or dine-in focused restaurants



### 4. rate

* **Type:** Float
* **Description:** Average rating of the restaurant (out of 5)
* **Notes:**

  * Converted from string to numeric format
  * Missing and invalid values were handled during cleaning
* **Usage:** Key metric for measuring restaurant performance



### 5. votes

* **Type:** Integer
* **Description:** Number of votes or reviews received
* **Usage:** Used as an indicator of popularity



### 6. location

* **Type:** String
* **Description:** Area where the restaurant is located
* **Usage:** Helps in location-based analysis



### 7. rest_type

* **Type:** String
* **Description:** Type of restaurant (e.g., Casual Dining, Cafe, Quick Bites)
* **Notes:**

  * Only the primary category has been retained for consistency
* **Usage:** Useful for segmenting restaurants by service type



### 8. cuisines

* **Type:** String
* **Description:** Main cuisine offered by the restaurant
* **Notes:**

  * Multiple cuisines were simplified to the primary cuisine
* **Usage:** Helps analyze cuisine preferences and trends



### 9. approx_costfor_two_people

* **Type:** Float
* **Description:** Approximate cost for two people
* **Notes:**

  * Converted from string format to numeric
  * Missing values handled during preprocessing
* **Usage:** Used for pricing and affordability analysis



### 10. listed_intype

* **Type:** String
* **Description:** Category under which the restaurant is listed (e.g., Buffet, Delivery)
* **Usage:** Helps understand the type of service offered



### 11. listed_incity

* **Type:** String
* **Description:** Broader area classification for listing
* **Usage:** Used for higher-level geographic grouping



## Additional Notes

* The original dataset contained additional columns such as address, phone, and reviews, which were removed as they were not required for analysis.
* Missing values were handled using appropriate methods to ensure consistency.
* Data types were standardized to support analysis and visualization.
* The final dataset is ready to be used in Tableau for building dashboards and deriving insights.


