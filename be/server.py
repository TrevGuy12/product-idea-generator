from flask import Flask
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate('./firebase.json')
firebase_admin.initialize_app(cred)

# Access Firestore database
db = firestore.client()

# Now you can use `db` to interact with your Firestore database


app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(debug=True)
