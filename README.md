CODE IMPLEMENTATION AND FILE EXPLAINATIONS:

---RUN FROM CONSOLE---
1. app.py - used command python app.py to launch the server on port 8000.
2. build_database.py - use command python build_database.py to remove all current data held within the tables and insert test data

---TABLE MANAGEMENT---
1. activity.py - holds CRUD operations for the activities table
2. preference.py - holds CRUD operations for the preference table
3. users.py - holds CRUD operations for the users table

---UTILITIES---
1. templates/home.html - default home page on launch
2. config.py - connects to database
3. Dockerfile - needed for docker image
4. models.py - holds table structure and relationships
5. requirements.txt - download list for background proccesses
6. swagger.yml - structure for link directories
