# BU Course Genie

A solution to minimizing the number of BU courses you have to take to fulfill HUB Requirements

## Installation and setup

#### Setting up virtual environment

######

    python3.9 -m pip install --upgrade pip
    python3.9 -m venv venv
    source venv/bin/activate

#### Necessary installations

######

    pip install Flask
    pip install python-dotenv
    pip install psycopg2
    pip install flask_sqlalchemy
    pip install ortools
    pip install flask_cors
    npm install -g @angular/cli

## Running code

You must use two separate terminals so you can run the frontend in one and the backend in the other.

######

    python3.9 app.py
    cd frontend
    ng serve

## Database interactions

1. Connecting to a certain DB as a specific user <br/>
   `psql -U username -d database_name`
2. Listing data tables <br/>
   `\dt`
3. Showing data table schema <br/>
   `\d table_name`
4. Showing roles of DB <br/>
   `\du`
5. Showing data within a data table <br/>
   `SELECT * FROM table_name;`

## Fixes to Common Issues

- Access to 127.0.0.1 was denied ( visit `chrome://net-internals/#sockets` and `Flush socket pools` )

## Updating scrape.py cookies (temporarily)

1. Navigate to MyBU Student --> Class Information --> Course Search
2. Inspect and open network tab
3. Click the "Search" button and right click on the request and copy as cURL
4. Paste it into a cURL to Python converter like [Curl Converter](https://curlconverter.com/) to get the Python request
5. Copy result into scrape.py where necessary

## Resources

[Geeks for Geeks](https://www.geeksforgeeks.org/flask-creating-first-simple-application/) <br/>
