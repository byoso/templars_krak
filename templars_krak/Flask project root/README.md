This boilerplate provides a Flask app with a user authentication ready to use.


Do not forget to migrate !!

```
#### Migrations
- Create the migration repository
```
$ flask db init
```
- make a new migration
```
$ flask db migrate -m "users table"
```
- apply the migration
```
$ flask db upgrade
```
