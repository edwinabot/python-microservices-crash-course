# Python & Microservices: Crash Course

In this repo we have a study case for building microservices with Python.

The exercise is to build a microservice which responds to main HTTP verbs, stores data on a DB and interacts with other services. All of this will guide us through an exploration of the Python programming language and some of it's ecosystem.

## The microservice

We will use [Falcon](https://falconframework.org/) to build our endpoints, SQLite as our DB and all of it will be tied up by [Python 3.6](https://www.python.org/).

The service will expose this endpoints:

```
    GET     /photo/list
    GET     /photo/{id}
    POST    /photo
    DELETE  /photo/{id}
```

We will build a component that must fetch photos from a [sandbox API](https://jsonplaceholder.typicode.com/) and store them on our DB. We will be implementing it so it runs using processes, threads or maybe event loops.

If the time is favorable to us we will be implementing the data access layer using [SQLAlchemy](https://www.sqlalchemy.org/).
