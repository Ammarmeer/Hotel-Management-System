from flask import Flask
from extensions import db, migrate
from routes.dashboard import dashboard_bp
from routes.rooms import rooms_bp
from routes.visitors import visitors_bp
from routes.visits import visits_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']='123455'
db.init_app(app)
migrate.init_app(app, db)

# Register Blueprints
app.register_blueprint(dashboard_bp, url_prefix='/')  # Set explicit prefix
app.register_blueprint(rooms_bp, url_prefix='/rooms')
app.register_blueprint(visitors_bp, url_prefix='/visitors')
app.register_blueprint(visits_bp, url_prefix='/visits')

if __name__ == "__main__":
    app.run(debug=True)
