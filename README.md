# Apache log file analysis using CouchDB

This is my little spare time project on log file analysis using [couchdb][cdb].

Currently, analysis is restricted to loading the parts of a log file entry
into a CouchDB Database. All views only operate on the simple facts of the
extracted data.

Now that I have successfully wrapped my mind around the concept of CouchApps I
am going to dig deeper into ways for more dynamic analysis. Currently I try to
figure a way for dynamically combining existing views...

# CouchApp

Finally I managed to get my head around the [CouchApp][couchapp] thing. The
*logHouse* directory contains a CouchApp doing all the analysis as the django
app, plus three more now.

The loader script has been extended to extract things like browser, os and bot
which are now added instead of the full agent string. These three are now
visible in the app.

[couchapp]: http://github.com/couchapp/couchapp

# Django-Application

*Note:* the development of the django app has been abandoned for the time
being. New stuff wil be in the CouchApp. The django app has been moved to
*django-log-house* .

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

 3. use httpagentparser to extract more information from the user agent

[cdb]: http://couchdb.apache.org
[dj]: http://www.djangoproject.com
[cdbkit]: http://www.couchdbkit.com
