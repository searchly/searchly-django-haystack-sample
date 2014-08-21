## Searchly.com Sample Django Haystack Application.

This example illustrates basic search features of Searchly.com (Search as a service powered by Elastisearch).

Each CRUD operation on documents is reflected to search index in real time.

To test Searchly's search features, login as admin, create a new document and search it.

Sample application is using [Haystack](http://haystacksearch.org/) moduler search for Django.

## Local Setup

Sample application requires a PostgreSQL and an Elasticsearch server up.

## Heroku Deployment

This sample can be deployed to Heroku with no change. With 2 steps application will be fully functional.

* Migrate database with `heroku run python manage.py syncdb`

* Install Searchly Elasticsearch Addon.

Deploy sample application with instructions of [Django Heroku documentation](https://devcenter.heroku.com/articles/getting-started-with-django).
