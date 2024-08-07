from app import db

class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(80), nullable=False)
    catalog_number = db.Column(db.String(80), nullable=False)
    class_section = db.Column(db.String(80), nullable=False)
    start_time = db.Column(db.String(80), nullable=False)
    end_time = db.Column(db.String(80), nullable=False)
    class_room = db.Column(db.String(80), nullable = True)
    instructor = db.Column(db.String(80), nullable = False)

    lab_parent_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    discussion_parent_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    schedule_id = db.Column(db.Integer, db.ForeignKey('schedules.id'))
    hub_credits_id = db.Column(db.Integer, db.ForeignKey('hub_credits.id'), nullable=False)

    labs = db.relationship('Course', backref=db.backref('lab_parent', remote_side=[id]), foreign_keys=[lab_parent_id])
    discussions = db.relationship('Course', backref=db.backref('discussion_parent', remote_side=[id]), foreign_keys=[discussion_parent_id])

    def __init__(self, course_name, catalog_number, class_section, start_time, end_time, instructor, class_room, lab_parent_id, discussion_parent_id, schedule_id, hub_credits_id) -> None:
        self.course_name = course_name
        self.catalog_number = catalog_number
        self.class_section = class_section
        self.start_time = start_time
        self.end_time = end_time
        self.instructor = instructor
        self.class_room = class_room
        self.lab_parent_id = lab_parent_id
        self.discussion_parent_id = discussion_parent_id
        self.schedule_id = schedule_id
        self.hub_credits_id = hub_credits_id

    def __repr__(self):
        return f"<Course(course_name='{self.course_name}', catalog_number={self.catalog_number}, class_section='{self.class_section}', time='{self.time}', lab_parent_id={self.lab_parent_id}, discussion_parent_id={self.discussion_parent_id}, schedule_id={self.schedule_id}, hub_credits_id={self.hub_credits_id})>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'course_name': self.course_name,
            'catalog_number': self.catalog_number,
            'class_section': self.class_section,
            'time': self.time  # Convert datetime to ISO format
        }

class Schedule(db.Model):
    __tablename__ = 'schedules'

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
    __tablename__ = 'hub_credits'

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