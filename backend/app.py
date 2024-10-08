from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect, text
from dotenv import load_dotenv
import os
from flask_migrate import Migrate
from flask_cors import CORS

from helpers.algorithm import solver

# Initialize SQLAlchemy and Migrate globally
db = SQLAlchemy()
migrate = Migrate()

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('POSTGRES_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})
db.init_app(app)
migrate.init_app(app, db)

@app.route('/')
def home():
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    return 'hi'

@app.route('/create_tables')
def create_tables():
    try:
        db.create_all()
        return 'Tables created successfully!'
    except Exception as e:
        return f'Failed to create tables: {str(e)}'

@app.route('/drop_tables')
def drop_tables():
    try:
        with app.app_context():
            db.metadata.reflect(bind=db.engine)
            inspector = inspect(db.engine)
            tables_before = inspector.get_table_names()
            print("Tables before drop:", tables_before)
            for tbl in reversed(db.metadata.sorted_tables):
                tbl.drop()
            
            tables_after = inspector.get_table_names()
            print("Tables after drop:", tables_after)
            
            if not tables_after:
                return 'Tables dropped successfully!'
            else:
                return f'Some tables were not dropped: {tables_after}'
    except Exception as e:
        return f'Failed to drop tables: {str(e)}'


@app.route('/scrape')
def scrape_courses():
    from helpers.newScrape import scraper
    response = scraper()
    return f'Did it work? {response["status"]}\n\n{response["body"]}'

@app.route('/write')
def write_courses():
    from helpers.write_courses import write_courses as wc
    from helpers.newScrape import scraper
    with app.app_context():
        result = scraper()
        if result['status'] == 200:
            # print(result['body'])
            return wc(result["body"])
        else:
            return 'ERROR SCRAPING'

@app.route('/table/<table>')
def see_table(table):
    inspector = inspect(db.engine)
    
    # Check if the table exists
    if table not in inspector.get_table_names():
        abort(404, description=f"Table '{table}' not found")

    # Query the table
    try:
        query = text(f"SELECT * FROM {table}")
        result = db.session.execute(query)
        columns = result.keys()
        data = [dict(zip(columns, row)) for row in result.fetchall()]
    except Exception as e:
        abort(500, description=f"Error querying table '{table}': {str(e)}")

    return jsonify(data)

# gives course details from database
def see_course(table, course_ids):
    inspector = inspect(db.engine)
    table = "courses"
    # Check if the table exists
    if table not in inspector.get_table_names():
        abort(404, description=f"Table '{table}' not found")

    # Query the table
    try:
        query = text(f"SELECT * FROM {table} WHERE id = ANY(:course_ids)")
        # Convert course_ids to a tuple
        result = db.session.execute(query, {"course_ids": course_ids})

        # Print the query and parameters for debugging
        print("Executing query:", query)
        print("With parameters:", {"course_ids": course_ids})

        columns = result.keys()
        data = [dict(zip(columns, row)) for row in result.fetchall()]
    except Exception as e:
        abort(500, description=f"Error querying table '{table}': {str(e)}")

    return data


@app.route('/solve/<int:maxCredits>/<hubString>')
def solve(maxCredits, hubString):
    courses = see_table('courses').get_json()
    return solver(maxCredits=maxCredits, hubString=hubString, courses=courses)

# actual api route for setting up all the backend and database support and then solving
@app.route('/api/setupsolve/<int:maxCredits>/<hubString>')
def setupsolve(maxCredits, hubString):
    try:
        # write_courses()
        # create_tables()
        # other setup steps necessary for the backend before calling solve
        return jsonify({"status": "success", "data": solve(maxCredits, hubString)}), 200
    except Exception as e:
        app.logger.error(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500
    
# route to return info about the courses selected by solver
@app.route('/api/courses/details/<courseIds>')
def course_details(courseIds):
    try:
        print("course ids", courseIds, "\n\n")
        course_id_arr = list(map(int, courseIds.split(',')))
        print("now in array form", course_id_arr)
        # return "currently testing"
        response = see_course("courses", course_ids=course_id_arr)
        print("response from seeing courses", response)
        data = response
        return jsonify({"status": "success", "data": data}), 200
    except Exception as e:
        app.logger.error(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

# check the database URI connection
@app.route('/health')
def health():
    return f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}"

# # test form post ability
# @app.route('/api/form', methods=['POST'])
# def handle_form():
#     data = request.get_json()
#     # Process the data
#     print("==============>", data)
#     return jsonify({"status": "success", "data": data})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('BACKEND_PORT'))
