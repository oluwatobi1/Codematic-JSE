**Great-Distance Api**
----
  _when hit will return the great-circle distance between two users given their latitudes and longitudes in decimal degrees(+/-DDD.DDDDD)._

* **URL**

  <https://codematiclocationapi.herokuapp.com/great_circle_distance/>

* **Method:**

  `GET`
  
*  **URL Params**

   _If URL params exist, specify them in accordance with name mentioned in URL section. Separate into optional and required. Document data constraints._

   **Required:**
 
   `latitude1=[integer]`
   
   `latitude2=[integer]`
   
   `longitude1=[integer]`
   
   `longitude2=[integer]`
   


* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ` ”XXXX.XX km”`
 
* **Error Response:**

  _There are a number of ways it can fail from wrongful parameters._

  * **Code:** 400 <br />
    **Content:** `{ error : "Descriptive error message" }`

 
* **Sample Call [curl]:**

  _Request:  curl -X GET "https://codematiclocationapi.herokuapp.com/great_circle_distance/?latitude1=55&longitude1=42&latitude2=33&longitude2=89"_

  _Request:>Response: “109.50 km._
  
  **Sample Call2 [python]:**

  `import requests`
  
  `url = "https://codematiclocationapi.herokuapp.com/great_circle_distance/?longitude1=45&longitude2=-34&latitude1=42&latitude2=87"`
  
  `payload='author=a%3Bldj&language=sterling&title=randome'`
  
    `headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}`
    `response = requests.request("GET", url, headers=headers, data=payload)`

    `print(response.text)`_

  _>Response: “109.50 km._


