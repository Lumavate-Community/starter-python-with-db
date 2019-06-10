## Requirements
You will need to set a valid Postgres connect string for the DATABASE_URL environment variable for this example to work.

## Adding a RESTful object
This is a guide to adding a restful object with a single property, name, within a python microservice.

To add a restful object, the first step is to add a migration. To add a migration, execute the following alembic command:
```bash
luma microservice-version exec "alembic revision -m Example"
```
### IMPORTANT:
When using an editable container, you must click the refresh button to see the file that is created by the alembic command.

This will generate a file inside app/alembic/versions. Inside this file, we will specify the upgrade and downgrade functions.
In the generated file (located under /app/alembic/versions) make sure the upgrade / downgrade methods are defined as follows:
```python
def upgrade():
    op.create_table('thing',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('name', sa.String(250), nullable=False),
        sa.Column('org_id', sa.BigInteger)
    )

def downgrade():
    op.drop_table('thing')
```
Then, run the following command to upgrade the table.
```bash
luma microservice-version exec "alembic upgrade head"
```

Then, we will define a model to represent a record inside of the 'thing' table. It belongs in the models directory.
```python
# /app/models/service.py

from flask import g
from app import db
from lumavate_service_util import make_id

class Thing(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    org_id = db.Column(db.BigInteger)

    @classmethod
    def get_all(cls):
        return cls.query.filter_by(org_id = g.org_id)

    @classmethod
    def get(cls, id):
        return cls.get_all().filter_by(id=id).first()

    def to_json(self):
        return {
            'id': make_id(self.id, self.__class__),
            'name': self.name
        }

```

Next, we create a controller to house any business logic for this object.  In this example we will be performing very stabdard
actions, so we will inherit from a base controller and will not need to override any methods.
```python
# /app/controllers/service.py

from lumavate_service_util import RestBehavior
import models

class Thing(RestBehavior):
  def __init__(self):
    super().__init__(models.Thing)
```


Finally, we must add routes to get, post, put, and delete these objects.  It's standard for the servide to support a '/' route, which provides a preview when viewed from within the designer.
```python
# /app/routes/service.py

from lumavate_service_util import lumavate_route, SecurityType, RequestType
from flask import render_template, g, request
from controllers import Thing

@lumavate_route('/', ['GET'], RequestType.page, [SecurityType.jwt])
def root():
  return render_template('home.html', logo='/{}/{}/discover/icons/microservice.png'.format(g.integration_cloud, g.widget_type))

@lumavate_route('/things', ['GET','POST'], RequestType.api, [SecurityType.none])
def allthings():
  if request.method == 'GET':
    return Thing().get_collection()
  else:
    return Thing().post()

@lumavate_route('/things/<int:id>', ['GET','PUT','DELETE'], RequestType.api, [SecurityType.none])
def onething():
  if request.method == 'GET':
    return Thing().get_single(id)
  elif request.method == 'PUT':
    return Thing().put(id)
  else:
    Thing().delete(id)
```
In this example, our routes do not require any authentication.

### IMPORTANT:
  When using an editable container, you must run the register routes command any time a route is created, deleted, or altered.
You may access this command in VScode through the command pallette. (ctrl-shift-p)/(cmd-shift-p).


You can read more about the container utility libraries at https://developer.lumavate.com

### Usage from Pagebuilder

Once this service is brought into an experience, it will be made available automatically via a JavaScript variable.  Following are example of how you can invoke the POST and GET routes, respectively:

```javascript
// Note m_service will be replaced with your actual service name

m_service.post('/things', data=JSON.stringify({'name': 'foo'}));

m_service.get('/things').then( (resp) => {
  console.log(resp);
})
```












