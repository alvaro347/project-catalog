* Project Item Catalog: Gallery *
-------------------------------------

* Introduction:
--------------

This application creates a item catalog of simple topics. It uses Python (Flask to create the server side), HTML, CSS and SQL.

1. The application it's base on an item catalog that have edit and delete features.
2. Users have to login in order to edit or delete elements of the database.
3. This item catalog is base on pictures so it allows picture upload with Flask modules.

The application uses Python 2 (for the server), HTML5 and CSS3 (for the web) and sqlalchemy for the databse.

* Contents
----------

	- project.py: the python file for the server side application.
	- database_setup.py: python file to create the custom item catalog database. This will include 3 tables (Gallery, Pictures and User)
  - gallery_elements.py: This will add predefine elements to the database.
	- imagegallery.db: this is the database itself in db format. This database will contain the tables: gallery, pictures and user.
	- README.md: readme file for know for about the application.
  - client_secrets.json: Google Json file for user login configurations.
  - static folder: will contain the CSS style file plus all the image files for the gallery.
  - templantes folder: Contains all the HTML files necessary for the project.

* Operating instructions
------------------------

FIRST OF ALL:

 - Add a google oauth2 api key to the "login.html" file where it says "YOUR-API-KEY-HERE"

Generate the databse (only if the databse file have been removed or you want to put it back to its original state):

  1. Delete the database from the root folder
  2. Run database_setup.py to generate the databse.
  3. Run gallery_elements.py to add all the elements to the database.

To run the python file and check the item catalog you will have to run it in a linux enviroment or virtual machine using vagrant.

	1. Navigate to the project folder copy the vagrant file from Udacity, and install the VM with the command: $ vagrant up
	2. When the process is finished run the command $ vagrant ssh. To log-in in the VM.
	3. To load the item catalog navigate to the directory containing the projec.py file and run it with $python project.py

To add new pictures or galleries:

  1. Login with a google account
  2. Press the "add" button and fill all the input forms.
  3. Upload a photo in PNG JPG format and hit submit.

To edit, delete a picture or gallery:

  1. Login with a google account
  2. Press the "edit" or "delete" button and fill all the input forms.
  3. Hit "submit" or "delete" to proceed.
