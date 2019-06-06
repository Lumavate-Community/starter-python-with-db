# Email Service

## Adding a new api Route

```python

@lumavate_route('/helloworld', ['GET'], RequestType.api, [SecurityType.none])
def helloworld():
  return "hello!"

```
Routes go in the routes directory.
To add a route to our microservice, we will use a function decorator similar to flask. However, the lumavate platform provides a special decorator with more functionality.
In this example, our route, /helloworld, only GET requests are allowed. It is an api route, and it does not require any authentication.

### IMPORTANT:
  When using an editable container, you must run the register routes command any time a route is created, deleted, or altered.
You may access this command in VScode through the command pallette. (ctrl-shift-p)/(cmd-shift-p).





## Adding a new api Route

```python

@lumavate_route('/helloworld', ['GET'], RequestType.api, [SecurityType.none])
def helloworld():
  return "hello!"

```
Routes go in the routes directory.
To add a route to our microservice, we will use a function decorator similar to flask. However, the lumavate platform provides a special decorator with more functionality.
In this example, our route, /helloworld, only GET requests are allowed. It is an api route, and it does not require any authentication.

### IMPORTANT:
  When using an editable container, you must run the register routes command any time a route is created, deleted, or altered.
You may access this command in VScode through the command pallette. (ctrl-shift-p)/(cmd-shift-p).








