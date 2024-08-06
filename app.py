from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect, text
from dotenv import load_dotenv
import os
from flask_migrate import Migrate

from helpers.scrape import fetch_and_write_response
from algorithm import solver

# Initialize SQLAlchemy and Migrate globally
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    load_dotenv()
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('POSTGRES_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
      
    db.init_app(app)
    migrate.init_app(app, db)
    
    
    from models import Course, Schedule, HubCredits  
    
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
    
    @app.route('/scrape')
    def scrape_courses():
        response = fetch_and_write_response()
        return f'Did it work? {response["status"]}'
    
    @app.route('/write')
    def write_courses():
        from write_courses import write_courses as wc
        with app.app_context():
            result = fetch_and_write_response()
            if result['status'] == 200:
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
    
    @app.route('/solve/<int:maxCredits>/<hubString>')
    def solve(maxCredits, hubString):
        courses = see_table('courses').get_json()
        return solver(maxCredits=maxCredits, hubString=hubString, courses=courses)
    
    @app.route('/health')
    def health():
        return f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}"
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
