
.. _FAQ_BASIC:


Why do I need pythonids?
------------------------
The module *pythonids* provides the information of the *Python* Syntax implementation
by one integer only.
Thus specific code segments could be easily addresses from within shared code whithout 
overall performance degradation, actually much faster than manually coding selection.
In addition there is no need for loading syntax and/or implementation specific code modules.

The performance impact within large loops - if at all - is kept minimal.

A prominent example is here the evolution of the *collections.namedtuple* within the 
syntax and implementation releases of *CPython-3.7*, which 
supports default values for the implementation of the *Python* syntax release *Python-3.7*
for *CPython* only since *CPython-3.7.0* / *CPython-3.7.4*, see [CHANGELOG370beta1]_ and [CHANGELOG374rc1]_. 
Thus a software component for *Python-3 <= 3.7.0 / 3.7.4* requires modifications, or an alternate module
like *namedtupledefs* [namedtupledefs]_.

The full history of the partially incompatible change at the time of writing:

* Changed the implementation strategy for collections.namedtuple() [CHANGELOG370alpha1a]_ [bpo-28638]_
* Fix misspelled attribute name in namedtuple / 3.7.4rc1; [issue36321]_ 
* Fix wrong usage of collections.namedtuple() [CHANGELOG370alpha3]_ [bpo-31325]_ 
* Optimize namedtuple creation / 3.7.0alpha1; [issue28638]_
* Python function can now have more than 255 parameters. [CHANGELOG370alpha1b]_ [bpo-18896]_ 
* Remove namedtuple 255 arguments restriction / 3.7.0alpha1; [issue18896]_
* [bpo-18896] see [issue18896]_ 
* [bpo-28638] see [issue28638]_ 
* [bpo-31325] see [issue31325]_ 
* [bpo-32320] see [issue32320]_ 
* [bpo-36321] see [issue36321]_ 
* collections.namedtuple() misspelled the name of an attribute [CHANGELOG374rc1]_ [bpo-36321]_ 
* collections.namedtuple() now supports default values. / 3.7.0beta1; [issue32320]_ 
* collections.namedtuple() now supports default values. [CHANGELOG370beta1]_ [bpo-32320]_ 
* req_rate is a namedtuple type rather than instance / 3.7.0alpha3; [issue31325]_

The provided patched set of libraries for a unified API on Python2 and Python3 (all releases):

* Standard library [namedutple-python3]_
* lib/collections [namedtuple]_
* patches of *collection.namedtuple* for Python2 [namedtupledefs2]_
* patches of *collection.namedtuple* for Python3 [namedtupledefs3]_
* patches of *collection.namedtuple* for Python3 [namedtupledefs]_



Why do I need pythonids.pydist?
-------------------------------

The module *pythonids.pydist* provides the combined information of the *Python* implementation
by one integer only.
This includes the distribution, the release, and the implemented syntax version.
Thus specific code segments could be easily addresses from within shared code whithout 
overall performance degradation, actually much faster than manually coding selection.
In addition there is no need for loading syntax and/or implementation specific code modules.
The performance impact within large loops - if at all - is kept minimal.

A prominent example is here the evolution of the *collections.namedtuple* within the 
syntax and implementation releases of *CPython-3.7*, which 
supports default values for the implementation of the *Python* syntax release *Python-3.7*
for *CPython* only since *CPython-3.7.0* / *CPython-3.7.4*, see [CHANGELOG370beta1]_ and [CHANGELOG374rc1]_. 
This is not available for the implementations of *IronPython* and *Jython* as they 
provide the syntax release *Python2.7*.
Thus a software components for these implementations require modifications, or an alternate module
like *namedtupledefs2* [namedtupledefs2]_.

Why yet another API?
--------------------
The provided API by *pythonids* is independent from the *Python* syntax reelases and the 
implementations, see :ref:`TESTED_OS_PYTHON`.
The API of the  *pythonids* is much more compact and designed for peformance on large number of calls e.g. 
from within loops.
The API provides detailed information on syntax and implementation by 16bit and 32bit values only, so is prepared
to be efficiently used on data center apps, client apps, as well as embedded and IoT systems 
e.g. by *MicroPython* [MicroPython]_ and *CircuitPython* [CircuitPython]_. 

