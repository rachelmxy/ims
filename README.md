# Inventory Management System
Backend Developer Coding Assignment for Kiratech

# Dependencies
1. Python3
2. Django
3. Django rest framework

# Setup Video + How To Use
Google drive: https://drive.google.com/file/d/1ibTpQBoqoqqlY-Ovt28lpxLC39QlDHPk/view?usp=sharing


Alternatively, view the written steps below
# Setup
1. Using command prompt, navigate to the 'project' directory (example: C:\Users\Hp\Downloads\ims-main\project\)
2. Start virtual environment with 'pipenv shell' command
3. Start server with 'py manage.py runserver' command
4. If not installed or if error message appears, install Pillow prior to running server with 'python -m pip install Pillow' command
5. If any errors occur (such as empty database), see below

# To load data into database (may not need)
1. Run command 'pipenv shell' in command prompt if not already in the virtual environment
2. Run command 'py manage.py loaddata supplier_data.json' first
3. Run command 'py manage.py loaddata inventory_data.json' first

# Sync database (may not need)
1. Run command 'py manage.py makemigrations
2. Run command 'py manage.py migrate'


# How to Use 
1. Run command 'pipenv shell' in command prompt if not already in the virtual environment
2. Run command 'py manage.py runserver' to start the server
3. At the page that appears at , click on any of the navigation items to navigate to the corresponding page
# At'ADMIN DASHBOARD'
--> username: admin
--> password: password123
--> email: admin@mail.com
Once logged in, CRUD operations on the Inventory model are able to be performed

# At 'INVENTORY LIST'
This page displays the full list of inventory items in the database. Click the 'View Item' link to load another page with the full details of a single item

# At 'API'
This page displays the response from the API query. Filter function is supported via URL query parameter. Example: http://127.0.0.1:8000/api/inventory/?name=Daily%20Repair%20Foam%20Cleanser will display the response for only the Daily Repair Foam Cleanser inventory item



# References
https://medium.com/backticks-tildes/lets-build-an-api-with-django-rest-framework-32fcf40231e5

https://stackoverflow.com/questions/35602049/how-to-insert-data-to-django-database-from-views-py-file

https://www.django-rest-framework.org/tutorial/quickstart/

https://www.django-rest-framework.org/api-guide/filtering/

https://stackoverflow.com/questions/47873707/django-rest-framework-filtering-against-the-url

https://www.geeksforgeeks.org/list-view-function-based-views-django/
	
https://www.youtube.com/watch?v=c2hbT0uIcOQ&ab_channel=TheNetNinja

https://www.youtube.com/watch?v=LAIVhl2CG8E&ab_channel=TheNetNinja

https://www.youtube.com/watch?v=QLL4KzFMfVw&ab_channel=ProblemSolvingPoint

https://stackoverflow.com/questions/51882627/how-to-link-css-to-html-in-django
