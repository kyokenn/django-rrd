django-rrd
==========

Web frontend to RRDtool based on Django

Requirements
============

* Python >= 3.0
* Django >= 1.7
* python-rrdtool >= 1.4.7

The recommended python-rrdtool fork [python-rrdtool](https://github.com/alertedsnake/python-rrdtool)


Installation
============

Install using PIP
-----------------

```
$ pip install django-rrd
```

Configuration
=============

Modify your settings.py
-----------------------

```python
INSTALLED_APPS = (
    ...
    'djangorrd',
    ...
)
```

Modify you urls.py
------------------

```python
urlpatterns = [
    ...
    url(r'^rrd/', include('djangorrd.urls', namespace='rrd')),
    ...
]
```

Create RRD
==========

Create RRD and graph using your django admin
--------------------------------------------

Feed RRD with a values
======================

You can feed RRD with a values by using one of the options:

RRDtool
-------

Use original rrdtool to update the RRD, for example:
```
$ rrdtool update path/to/file.rrd N:1234
```

./manage.py
-----------

Use management command rrd_poller to update the RRD.
The command's syntax is the same as the "rrdtool update" tool,
but you have to replace a file path with a RRD name defined in django admin.
```
$ ./manage.py rrd_poller name N:1234
```

Custom python script
--------------------

Invoke rrd.update(args) from your python script, for example:
```
from djangorrd.models import RRD
rrd = RRD.objects.get(name='name')
rrd.update(['N:1234'])
```

Display graph
=============

Open a link "/rrd/graph/NAME/" to get a graph.
