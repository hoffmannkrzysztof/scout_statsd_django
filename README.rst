===================
Scout StatsD Django 
===================

The ``scout_statsd_django`` extension instruments Django applications served by Django with StatsD. This extension was forked from `django_statsd <https://github.com/andymckay/django-statsd>`_ is maintained by `Scout <https://scoutapp.com>`_ for our `hosted StatsD <https://scoutapp.com/statsd>`_ service but is compatible with any StatsD collector. 


.. image:: https://dl.dropboxusercontent.com/u/2333541/django_dash.png



Original project documentation is on `Read the Docs <https://django-statsd.readthedocs.org/>`_.

----------------
Reported Metrics
----------------

The following metrics are reported:

* Response code rates (2XX, 3XX, 4XX, 5XX, etc)
* Response time
* Request throughput

-------------------
Django Installation
-------------------

Add the package:

    ``pip install git+git://github.com/scoutapp/scout_statsd_django.git``

Next, update ``setttings.py`` and add the following middleware to the top of the list:
    
::
    MIDDLEWARE_CLASSES = (
      'django_statsd.middleware.StatsMiddleware', ) 
      + MIDDLEWARE_CLASSES

----------------
Using with Scout
----------------

Just install the `Scoutd <http://help.scoutapp.com/docs/agent>`_ agent on the host(s) serving the app to see the Django metrics in the Scout UI.

-----
Scope
-----

This extension is laser-focused on Django-related metrics. Other ``scout_statsd_X`` extensions instrument different areas of code and frameworks.

--------------------
Questions? Feedback?
--------------------

`Create an issue <https://github.com/scoutapp/scout_statsd_rack/issues>`_ or shoot an email to `support@scoutapp.com <mailto: support@scoutapp.com>`_

------------
Contributing
------------

1. Fork it
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

-------
License
-------

BSD and MPL

Portions of this are from commonware:

https://github.com/jsocol/commonware/blob/master/LICENSE

.. |Build Status| image:: https://travis-ci.org/andymckay/django-statsd.svg?branch=master
   :target: https://travis-ci.org/andymckay/django-statsd
