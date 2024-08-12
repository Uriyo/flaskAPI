from flask import Flask
from config import Config
from models import db, bcrypt
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from routes.user_routes import user_bp
from routes.contact_routes import contact_bp

app.register_blueprint(user_bp)
app.register_blueprint(contact_bp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
