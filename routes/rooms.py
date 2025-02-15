from flask import render_template, request, redirect, url_for
from models import Room
from routes import rooms_bp
# from app import db
from extensions import db

@rooms_bp.route('/rooms')
def view_rooms():
    rooms = Room.query.all()
    return render_template('rooms.html', rooms=rooms)

@rooms_bp.route('/add-room', methods=['GET', 'POST'])
def add_room():
    if request.method == 'POST':
        room_number = request.form['room_number']
        washroom_seat_type = request.form['washroom_seat_type']
        floor_number = request.form['floor_number']
        condition = request.form['condition']
        single_bed = request.form['single_bed']
        double_bed = request.form['double_bed']
        status = "Available"

        new_room = Room(room_number=room_number, washroom_seat_type=washroom_seat_type,
                        floor_number=floor_number, condition=condition,
                        single_bed=single_bed, double_bed=double_bed, status=status)

        db.session.add(new_room)
        db.session.commit()
        return redirect(url_for('rooms.view_rooms'))
    
    return render_template('add_room.html')
