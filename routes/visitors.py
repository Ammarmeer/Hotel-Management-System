from flask import render_template, request, redirect, url_for
from models import Visitor, Room
from routes import visitors_bp
from extensions import db

@visitors_bp.route('/visitors')
def view_visitors():
    visitors = Visitor.query.all()
    return render_template('visitors.html', visitors=visitors)


@visitors_bp.route('/add-visitor', methods=['GET', 'POST'])
def add_visitor():
    if request.method == 'POST':
        name = request.form['name']
        father_name = request.form['father_name']
        cnic = request.form['cnic']
        phone = request.form['phone']
        address = request.form['address']
        
        # ✅ Handle missing 'room' field safely
        room_id = request.form.get('room')  
        room_id = int(room_id) if room_id else None  # Convert to int if exists

        new_visitor = Visitor(
            name=name, 
            father_name=father_name, 
            cnic=cnic, 
            phone=phone, 
            address=address,
            room_id=room_id  # ✅ Store room_id
        )

        db.session.add(new_visitor)
        db.session.commit()
        return redirect(url_for('visitors_bp.view_visitors'))
    
    rooms = Room.query.filter_by(status="Free").all()  # ✅ Get available rooms
    return render_template('add_visitor.html', rooms=rooms)
