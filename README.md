# InterimPrototype
This repo stores the code for my Interim prototypes - the Django Database and the Maths Quiz and a dump of the Django Database Data

# Maths Quiz
Simple Maths Quiz created in Python. 
Main class is mathsQuiz and will run automatically, but if needed can be called by using mathsQuiz().

# ProtoTest
Code created for the Django backend Database, most of the code was generated automatically when the Django file was created, but the files
- models.py
- admin.py
- and prototest/urls.py

were all modified to create the database used for the prototype.

The models.py file contains the models used in the database (similar to the database tables).

The admin.py file added the models to the django administration site.

The prototest/urls.py files just added the admin and proto apps to the main localhost url.

# Django Dump Data
dump of the Django database data in a json file, made by running the command  
*manage.py dumpdata proto*
