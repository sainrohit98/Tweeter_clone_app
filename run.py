from flask import Flask
from posts.routes import posts
from weather.routes import weather
from extentions import db


app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
print(app.config)
app.register_blueprint(posts)
app.register_blueprint(weather)
db.init_app(app)
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
