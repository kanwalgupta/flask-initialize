from flask import Flask, jsonify
import psycopg2
from api.models.passengers import Passenger

def create_app(database, user, password):
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE = database,
        USER = user,
        PASSWORD = password
    )

    @app.route('/')
    def index():
        return 'Welcome to airlines !'
    
    @app.route('/passengers')
    def passengers():
        conn = psycopg2.connect(database = database , user = user, password = password)
        cursor = conn.cursor()
        cursor.execute('select * from passengers')
        passengers_records = cursor.fetchall()
        return [Passenger(record).__dict__ for record in passengers_records]
    
    return app
