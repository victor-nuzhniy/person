# person

## Installation

### Sensitive data

1. Create in the project root (or obtain from team member) an `.env` file with 
environment variables required by application.
    SECRET_KEY =
    ALLOWED_HOST=
    DEBUG=


### Local run in docker container using docker-compose

1. Ensure `.env` file has at least `POSTGRES_USER`, `POSTGRES_PASSWORD` and 
    `POSTGRES_DB` variables set to any string values.
2. Run _postgres_ in docker containers:

       docker-compose up  # run all services defined in docker-compose file


### Performing commits

1. Pre-commit hook installed, settings are in .pre-commit-config.yaml
2. To instantiate new hook settings change .pre-commit-config.yaml file
     and run     pre-commit install
3. To bypass hook checking run      git commit -m "..." --no-verify


### Setup database using sql files

For work with application, you need to setup your database in docker container. To perform this:

1. While postgres docker container is running, enter it (use separate terminal):

       docker exec -it person bash

2. Enter inside psql terminal (inside your container):

       psql -U postgres

3. Create database for use it in our application and use it (inside psql terminal):

       CREATE DATABASE network;
       \c person;

### Performing tests

For testing application there is need to use pytest and it's plugings.
There is need to always check amount of test cases and their covering.

1. To perform created test cases, use command:

       pytest --cov