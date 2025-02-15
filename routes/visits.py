from flask import render_template, request, redirect, url_for
from models import Visit, Room
from routes import visits_bp
from extensions import db

@visits_bp.route('/visits')
def view_visits():
    """View all visits."""
    visits = Visit.query.all()
    return render_template('visits.html', visits=visits)

def get_free_rooms():
    """Fetch free rooms from the database using SQLAlchemy."""
    return Room.query.filter_by(status='Free').all()  # ✅ Fixed status case

@visits_bp.route('/add-visit', methods=['GET', 'POST'])
def add_visit():
    """Add a new visit."""
    if request.method == 'POST':
        print("Incoming form data:", request.form)  # Debugging

        try:
            date = request.form['date']
            vehicle_number = request.form['vehicle_number']
            persons = int(request.form['persons'])
            checkin_date = request.form['checkin_date']
            checkout_date = request.form['checkout_date']
            visitor_id = int(request.form['visitor_id'])

            # ✅ Convert selected_room_ids to integers
            selected_room_ids = list(map(int, request.form.getlist('rooms')))
            selected_rooms = Room.query.filter(Room.id.in_(selected_room_ids)).all()

            # ✅ Store room IDs as a JSON list
            room_data = [room.id for room in selected_rooms]

            new_visit = Visit(
                date=date,
                vehicle_number=vehicle_number,
                persons=persons,
                rooms=room_data,  # JSON list of room IDs
                checkin_date=checkin_date,
                checkout_date=checkout_date,
                visitor_id=visitor_id
            )

            db.session.add(new_visit)

            # ✅ Mark selected rooms as 'Booked'
            for room in selected_rooms:
                room.status = 'Booked'

            db.session.commit()

            return redirect(url_for('visits_bp.view_visits'))

        except Exception as e:
            print("🔥 Error occurred:", e)  # Debugging
            return f"An error occurred: {e}", 500  # Show error in the browser

    free_rooms = get_free_rooms()
    return render_template('add_visit.html', free_rooms=free_rooms)
