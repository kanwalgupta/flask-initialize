from api import create_app
from settings import DATABASE,USER, PASSWORD

app = create_app(DATABASE, USER, PASSWORD)

app.run(debug= True)