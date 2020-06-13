SQLObject Adapter for PyCasbin
====

[![Build Status](https://www.travis-ci.org/pycasbin/sqlobject-adapter.svg?branch=master)](https://www.travis-ci.org/pycasbin/sqlobject-adapter)
[![Coverage Status](https://coveralls.io/repos/github/pycasbin/sqlobject-adapter/badge.svg)](https://coveralls.io/github/pycasbin/sqlobject-adapter)
[![Version](https://img.shields.io/pypi/v/casbin_sqlobject_adapter.svg)](https://pypi.org/project/casbin_sqlobject_adapter/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/casbin_sqlobject_adapter.svg)](https://pypi.org/project/casbin_sqlobject_adapter/)
[![Pyversions](https://img.shields.io/pypi/pyversions/casbin_sqlobject_adapter.svg)](https://pypi.org/project/casbin_sqlobject_adapter/)
[![Download](https://img.shields.io/pypi/dm/casbin_sqlobject_adapter.svg)](https://pypi.org/project/casbin_sqlobject_adapter/)
[![License](https://img.shields.io/pypi/l/casbin_sqlobject_adapter.svg)](https://pypi.org/project/casbin_sqlobject_adapter/)

SQLObject Adapter is the [SQLObject](http://www.sqlobject.org/index.html) adapter for [PyCasbin](https://github.com/casbin/pycasbin). With this library, Casbin can load policy from SQLObject supported database or save policy to it.

The current supported databases are:

- PostgreSQL
- MySQL
- SQLite
- Microsoft SQL Server
- Firebird
- Sybase
- MAX DB
- pyfirebirdsql

## Installation

```
pip install casbin_sqlobject_adapter
```

## Simple Example

```python
import casbin_sqlobject_adapter
import casbin

adapter = casbin_sqlobject_adapter.Adapter('sqlite:///test.db')

e = casbin.Enforcer('path/to/model.conf', adapter, True)

sub = "alice"  # the user that wants to access a resource.
obj = "data1"  # the resource that is going to be accessed.
act = "read"  # the operation that the user performs on the resource.

if e.enforce(sub, obj, act):
    # permit alice to read data1casbin_sqlalchemy_adapter
    pass
else:
    # deny the request, show an error
    pass
```


### Getting Help

- [PyCasbin](https://github.com/casbin/pycasbin)

### License

This project is licensed under the [Apache 2.0 license](LICENSE).
