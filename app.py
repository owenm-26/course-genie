from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

# Configure the PostgreSQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('POSTGRES_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(80), unique=True, nullable=False)
    catalog_number = db.Column(db.Integer, unique=True, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    labs = db.relationship('Course', backref='lab_parent', remote_side=[id])
    discussions = db.relationship('Course', backref='discussion_parent', remote_side=[id])
    schedule_id = db.Column(db.Integer, db.ForeignKey('schedule.id'))
    hub_credits_id = db.Column(db.Integer, db.ForeignKey('hub_credits.id'))

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    monday = db.Column(db.Boolean, nullable=False)
    tuesday = db.Column(db.Boolean, nullable=False)
    wednesday = db.Column(db.Boolean, nullable=False)
    thursday = db.Column(db.Boolean, nullable=False)
    friday = db.Column(db.Boolean, nullable=False)
    saturday = db.Column(db.Boolean, nullable=False)
    sunday = db.Column(db.Boolean, nullable=False)
    courses = db.relationship('Course', backref='schedule')

class HubCredits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    historical_context = db.Column(db.Boolean, nullable=False)  # 'HUB-HCO'
    individual_in_community = db.Column(db.Boolean, nullable=False)  # 'HUB-IIC'
    research_and_information = db.Column(db.Boolean, nullable=False)  # 'HUB-RIL'
    social_inquiry_2 = db.Column(db.Boolean, nullable=False)  # 'HUB-SO2'
    global_citizenship = db.Column(db.Boolean, nullable=False)  # 'HUB-GCI'
    writing_intensive = db.Column(db.Boolean, nullable=False)  # 'HUB-WIN'
    ethical_reasoning = db.Column(db.Boolean, nullable=False)  # 'HUB-ETR'
    critical_thinking = db.Column(db.Boolean, nullable=False)  # 'HUB-CRT'
    creativity_and_innovation = db.Column(db.Boolean, nullable=False)  # 'HUB-CRI'
    teamwork_and_collaboration = db.Column(db.Boolean, nullable=False)  # 'HUB-TWC'
    scientific_inquiry_1 = db.Column(db.Boolean, nullable=False)  # 'HUB-SI1'
    digital_multimedia = db.Column(db.Boolean, nullable=False)  # 'HUB-DME'
    oral_and_signed_communication = db.Column(db.Boolean, nullable=False)  # 'HUB-OSC'
    aesthetic_exploration = db.Column(db.Boolean, nullable=False)  # 'HUB-AEX'
    philosophical_inquiry = db.Column(db.Boolean, nullable=False)  # 'HUB-PLM'
    first_year_writing = db.Column(db.Boolean, nullable=False)  # 'HUB-FYW'
    courses = db.relationship('Course', backref='hub_credits')

    def __repr__(self):
        return f'<HubCredits {self.id}>'

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

@app.route('/health')
def health():
    return f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}"

if __name__ == '__main__':
    app.run(debug=True)