# Apache log file analysis using CouchDB

This is my little spare time project on log file analysis using [couchdb][cdb].

Currently, analysis is restricted to loading the parts of a log file entry
into a CouchDB Database. All views only operate on the simple facts of the
extracted data.

# Django-Application

A first, very rough [django][dj] application is in the *log_house* directory.
Installing is as easy as creating a symbolic link in your project directory.
The actual database name is configured in the *log_house/settings.py* module.

# Loader

A separate script ( *loader* ) is responsible for loading and extracting the
data. If you want to use a different database name, change the last line.

# Dependencies

Besides the obvious (Django) you will need to install [couchdbkit][cdbkit].

# TODO

 1. move or copy parts of the configuration from the application's
     *settings.py* to the projects *settings.py*

 2. break up the loader and make the extraction of information more modular

[cdb]: http://couchdb.apache.org
[dj]: http://www.djangoproject.com
[cdbkit]: http://www.couchdbkit.com
