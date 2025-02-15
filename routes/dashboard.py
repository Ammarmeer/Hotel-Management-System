from flask import Blueprint, render_template
from models import Room, Visit
from extensions import db
from sqlalchemy.sql import func

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
def dashboard():
    free_rooms = Room.query.filter_by(status="Free").count()  # ✅ Fixed status case
    booked_rooms = Room.query.filter_by(status="Booked").count()

    # ✅ Fixed AttributeError (checkin_date instead of check_in_date)
    today_checkins = Visit.query.filter(Visit.checkin_date == func.current_date()).count()
    today_checkouts = Visit.query.filter(Visit.checkout_date == func.current_date()).count()
    will_checkout_today = Visit.query.filter(Visit.checkout_date == func.current_date()).count()

    return render_template('dashboard.html', 
                           free_rooms=free_rooms, 
                           booked_rooms=booked_rooms,
                           today_checkins=today_checkins, 
                           today_checkouts=today_checkouts,
                           will_checkout_today=will_checkout_today)
