# djangoApiSearch
**djangoApiSearch** is API for scraping different goods in such stores as _Eldorado, Stylus and MOYO_

**djangoApiSearch** has got  _Django Admin Panel_ and _sqlite3_ database, but can be connected _postgresql_

**API** has got documentation _''Swagger''_
## Installation
* Create django project
* Create virtual environment
* Download this repository and put in project
* Install `requirements.txt`
```python
pip install -r requirements.txt
```
* Make migrate
```python
python manage.py makemigrations
python manage.py migrate
```
* Create superuser
```python
python manage.py createsuperuser
```
## Usage
You need to send post request on **_localhost/api/search_** with arguments: **name** and **search**. 

The API response will be a dictionary of stores in JSON form with a list for names, links and prices of goods.

The API also save search results in a database with the user name and search query.

To administer data, you need to login _django admin_ **_localhost/admin_**.
## Example
**Django Admin Panel** | [**_localhost/admin_**](http://103.45.247.96/admin/) | username - **_admin_** password - **_djangoApiSearch_**
--- | --- | ---
**API** for search of goods | [**_localhost/api/search_**](http://103.45.247.96/api/search/) | 
**''Swagger''** | [**_localhost/doc_**](http://103.45.247.96/doc) | 
