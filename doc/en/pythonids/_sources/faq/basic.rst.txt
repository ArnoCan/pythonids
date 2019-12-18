
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

