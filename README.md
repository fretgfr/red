# RED - Real Estate Database

## About

This repository houses the code for our database design project, in which we decided to create an application that utilizes a database to allow the posting of real esate listings with an online user interface.

## Running

### Pre-requisites 

- MySQL Server Running locally or remotely
- [Python](https://python.org/downloads) 3.9+
- flask
- mysql-connector-python

Install [Python](https://python.org/) 3.9+ on your system then use the `pip` package manager to install the flask and mysql-connector-python packages.

#### On Windows
`py -3 -m pip install flask mysql-connector-python`

#### On macOS/Linux

`python3 -m pip install flask mysql-connector-python`


### Setup

Clone the repository to your local machine and create a file named `config.json` in the directory with `app.py` with the following format:

```json
{
    "user": "username",
    "password": "password",
    "database": "databasename",
    "host": "server.host.ip.address"
}
```

Replace the placeholders with the information necessary to connect to your running MySQL server.

You should now be ready to run the application to test it out! Simply run `app.py` with python and connect to the testing server at `127.0.0.1:5000`.