Django+Cloud SQL Google App Engine sample
=========================================

This sample demonstrates how to setup continuous integration and deployment for a Django+Cloud SQL project deployed on Google App Engine.

For more detailed documentation, please see Shippable's continuous deployment section: http://docs.shippable.com/ci_overview/

This sample is built for Shippable, a docker based continuous integration and delivery platform.

Here's how to get this sample app up and running on Google App Engine:
1. [Create a project](https://cloud.google.com/appengine/docs/python/console/#create) on Google Cloud Platform. Make sure you download and save the private JSON key created for the service account. If one is not automatically created for you, you can [generate](https://cloud.google.com/storage/docs/authentication#generating-a-private-key) one.
2. [Create a Cloud SQL Instance](https://cloud.google.com/appengine/docs/python/cloud-sql/#create).
3. In that instance, [create a database](https://cloud.google.com/sql/docs/create-database), named "django_test".
4. Give your project [access](https://cloud.google.com/sql/docs/dev-access#gaev1-csqlv1) to that CloudSQL instance.
5. In the Google Cloud Platform API Manager, enable these two APIs for your project: App Engine Admin API, and Google Cloud SQL API.
6. In your local environment, [configure](https://cloud.google.com/sql/docs/mysql-client) MySQL Client to connect to your Cloud SQL instance.
7. Once connected, add a table to your Cloud SQL django_test database, with the following command: `CREATE TABLE django_cloudsql_score (score INT, timestamp DATETIME, id SERIAL NOT NULL PRIMARY KEY);`
8. Update the database host (line 78) and instance (line 89) in `settings.py`.
9. Update the project name (line 26) in `shippable.yml`.
10. [Enable this project](http://docs.shippable.com/gs_ci_sample/#enable-a-project) on Shippable.
11. Encrypt the JSON private key for your service account as a [secure variable](http://docs.shippable.com/ci_configure/#secure-variables) for your project. When encrypting, use this format: `SERVICE_ACCOUNT_KEY='{"your": "json key here"}'`. Replace the existing secure variable (line 13) in `shippable.yml` with your secure variable.
12. Make sure you've pushed your code to your source provider, and trigger a build on Shippable. This build will deploy your app! Go to https://your-project-name-here.appspot.com/ to see your project live.

It's worth noting that this sample project uses the [Google Cloud SDK](https://cloud.google.com/sdk/gcloud-app) functionality for deploying and managing Google App Engine projects. While this functionality is still in beta, we've found that it's a powerful and easy way to trigger deployments directly from a successful build. The Python SDK for App Engine does not allow for proper authentication from within the build environment.
