from flask import Blueprint

dashboard_bp = Blueprint('dashboard', __name__)
rooms_bp = Blueprint('rooms', __name__)
visitors_bp = Blueprint('visitors', __name__)
visits_bp = Blueprint('visits', __name__)
