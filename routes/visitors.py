from flask import flash, render_template, request, redirect, url_for
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
        
        room_id = request.form.get('room')  
        room_id = int(room_id) if room_id else None

        # Check if CNIC already exists
        existing_visitor = Visitor.query.filter_by(cnic=cnic).first()
        if existing_visitor:
            flash('A visitor with this CNIC already exists!', 'danger')
            return redirect(url_for('visitors.add_visitor'))

        # Add new visitor
        new_visitor = Visitor(
            name=name, 
            father_name=father_name, 
            cnic=cnic, 
            phone=phone, 
            address=address,
            room_id=room_id
        )

        try:
            db.session.add(new_visitor)
            db.session.commit()
            flash('Visitor added successfully!', 'success')
            return redirect(url_for('visitors.view_visitors'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
            return redirect(url_for('visitors.add_visitor'))
    
    rooms = Room.query.filter_by(status="Free").all()
    return render_template('add_visitor.html', rooms=rooms)

