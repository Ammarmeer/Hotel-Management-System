from flask import flash, render_template, request, redirect, url_for
from models import Room, RoomStatus
from routes import rooms_bp
from extensions import db
@rooms_bp.route('/rooms')
def view_rooms():
    rooms = Room.query.all()
    return render_template('rooms.html', rooms=rooms)



@rooms_bp.route('/add-room', methods=['GET', 'POST'])
def add_room():
    if request.method == 'POST':
        room_number = request.form.get('room_number', '').strip()
        washroom_seat_type = request.form.get('washroom_seat_type', '').strip()
        floor_number = request.form.get('floor_number', '').strip()
        condition = request.form.get('condition', '').strip()
        single_bed = request.form.get('single_bed', '').strip()
        double_bed = request.form.get('double_bed', '').strip()
        status = RoomStatus.FREE  # Use the Enum directly

        # Validate input
        if not room_number or not washroom_seat_type or not floor_number or not condition:
            flash('All fields are required!', 'danger')
            rooms = Room.query.all()
            return render_template('add_room.html', rooms=rooms)

        if not single_bed.isdigit() or not double_bed.isdigit():
            flash('Single Bed and Double Bed must be numeric values!', 'danger')
            rooms = Room.query.all()
            return render_template('add_room.html', rooms=rooms)

        if washroom_seat_type not in ['English', 'Indian']:
            flash('Invalid washroom seat type!', 'danger')
            rooms = Room.query.all()
            return render_template('add_room.html', rooms=rooms)

        # Check for duplicate room_number
        existing_room = Room.query.filter_by(room_number=room_number).first()
        if existing_room:
            flash('A room with this room number already exists!', 'danger')
            rooms = Room.query.all()
            return render_template('add_room.html', rooms=rooms)

        try:
            # Create new room
            new_room = Room(
                room_number=room_number,
                washroom_seat_type=washroom_seat_type,
                floor_number=floor_number,
                condition=condition,
                single_bed=int(single_bed),
                double_bed=int(double_bed),
                status=status
            )

            # Add to the database
            db.session.add(new_room)
            db.session.commit()
            flash('Room added successfully!', 'success')
            return redirect(url_for('rooms.view_rooms'))

        except Exception as e:
            # Rollback in case of an error
            db.session.rollback()
            flash(f'Error adding room: {str(e)}', 'danger')
            rooms = Room.query.all()
            return render_template('add_room.html', rooms=rooms)

    # GET request: Render the form
    rooms = Room.query.all()
    return render_template('add_room.html', rooms=rooms)
