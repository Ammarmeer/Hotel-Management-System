from extensions import db

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(50), unique=True, nullable=False)
    washroom_seat_type = db.Column(db.String(10), nullable=False)  # English or Indian
    floor_number = db.Column(db.String(50), nullable=False)
    condition = db.Column(db.String(50), nullable=False)
    single_bed = db.Column(db.Integer, nullable=False)
    double_bed = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)  # Free, Booked

    # ✅ Relationship with Visitors
    visitors = db.relationship('Visitor', back_populates='room')

class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    father_name = db.Column(db.String(100), nullable=False)
    cnic = db.Column(db.String(15), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=True)
    room = db.relationship('Room', back_populates='visitors')
    visits = db.relationship('Visit', back_populates='visitor', cascade="all, delete-orphan")

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    vehicle_number = db.Column(db.String(20), nullable=False)
    persons = db.Column(db.Integer, nullable=False)
    rooms = db.Column(db.JSON, nullable=False)
    checkin_date = db.Column(db.Date, nullable=False)  # ✅ Fixed field name
    checkout_date = db.Column(db.Date, nullable=False)  # ✅ Fixed field name

    visitor_id = db.Column(db.Integer, db.ForeignKey('visitor.id'), nullable=False)
    visitor = db.relationship('Visitor', back_populates='visits')

class VisitInformation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_number = db.Column(db.String(50), nullable=True)
    checkin_date = db.Column(db.DateTime, nullable=False)
    checkout_date = db.Column(db.DateTime, nullable=True)
    men = db.Column(db.Integer, nullable=False)
    women = db.Column(db.Integer, nullable=False)
    children = db.Column(db.Integer, nullable=False)
    total_people = db.Column(db.Integer, nullable=False)

    visit_id = db.Column(db.Integer, db.ForeignKey('visit.id'), nullable=False)
    visit = db.relationship('Visit', backref='visit_info')
