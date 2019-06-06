


## Adding a RESTful object

This is a guide to adding a restful object with a single property, name, within a python microservice.

To add a restful object, the first step is to add a migration. To add a migration, execute the following alembic command:
```bash
luma microservice-version exec "alembic revision -m Example"
```
This will generate a file inside app/alembic/versions. Inside this file, we will specify the upgrade and downgrade functions.
```python
def upgrade():
    op.create_table('stuff',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('name', sa.String(250), nullable=False),
        sa.Column('org_id', sa.BigInteger)
    )

def downgrade():
    op.drop_table('stuff')
```
Then, run the following command to upgrade the table.
```bash
luma microservice-version exec "alembic upgrade head"
```


Then, we will define a model to represent a record inside of the stuff table. It belongs in the models directory.
```python
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
    @classmethod
    def post(cls):
        thing = Thing(name = request.form['name'],org_id = g.org_id)
        db.session.add(thing)
        db.session.flush()
        return thing
    @classmethod
    def delete(cls,id):
        cls.get(id).delete()
        db.session.commit()
    @classmethod
    def put(cls,id):
        thing = cls.get(id)
        if 'name' in request.form:
            thing.name = request.form['name']
            db.session.flush()
        return thing

    def to_json(self):
        return {
            'id': make_id(self.id, self.__class__),
            'name': self.name
        }
```
Finally, we must add routes to get, post, put, and delete these objects.
```python
@lumavate_route('/things', ['GET','POST'], RequestType.api, [SecurityType.none])
def allthings():
  if request.method == 'GET':
    return Thing().get_all()
  else:
    return Thing().post()

@lumavate_route('/things/<int:id>', ['GET','PUT','DELETE'], RequestType.api, [SecurityType.none])
def onething():
  if request.method == 'GET':
    return Thing().get(id)
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












