import pytest
from api import create_app
import json
from settings import TEST_DATABASE, USER, PASSWORD
from api.models.passengers import Passenger
from src.connection import *

passenger_records = [['kanwal', 'gupta', 'male', 34], ['charvi', 'gupta', 'female', 1]]
passenger_columns = ['first_name', 'last_name', 'gender', 'age']
@pytest.fixture(scope = 'module')
def app():
    flask_app = create_app(TEST_DATABASE, USER, PASSWORD)
    with flask_app.app_context():
        

        

        conn = build_connection(TEST_DATABASE, USER, PASSWORD)
        cursor = get_cursor(conn)
        add_records(cursor, 'passengers', passenger_columns, passenger_records[0])
        add_records(cursor, 'passengers', passenger_columns, passenger_records[1])

        conn.commit()
        close_conn(conn)

        yield flask_app

        with flask_app.app_context():
            close_conn(conn)
            conn = build_connection(TEST_DATABASE, USER, PASSWORD)
            cursor = get_cursor(conn)
            drop_records(cursor, 'passengers')
            conn.commit()
            close_conn(conn)

@pytest.fixture
def client(app):
    return app.test_client()

def test_root(client):
    response = client.get('/')
    assert b'Welcome to airlines !' in response.data

def test_passengers(client):
    response = client.get('/passengers')
    
    id_passenger_records = [[*record, index+1] for index,record in enumerate(passenger_records)]
    id_passenger_columns = [*passenger_columns, 'id']
    expected = [dict(zip(id_passenger_columns, record)) for record in id_passenger_records]
    assert json.loads(response.data) == expected


