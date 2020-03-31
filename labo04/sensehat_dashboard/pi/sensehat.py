from sense_hat import SenseHat
import firebase_admin
from firebase_admin import credentials, firestore
import threading


#constants
COLLECTION = 'raspberry'
DOCUMENT = 'student pi'

#firebase
cred = credentials.Certificate("./config/iotlabo03-firebase-adminsdk-2u6kd-7ad4e729f6.json")
firebase_admin.initialize_app(cred)


#senseHat
sense = SenseHat()
sense.set_imu_config(False,False,False)
sense.clear()

def update_sensehat(doc_snapshot, changes, read_time):
	for doc in doc_snapshot:
		doc_readable = doc.to_dict()
		print(doc_readable)


# connect firestore
db = firestore.client()
pi_ref = db.collection(COLLECTION).document(DOCUMENT)
pi_watch = pi_ref.on_snapshot(update_sensehat)

#app



def update_in_firebase():
	temperature = sense.get_temperature()
	pressure = sense.get_pressure()
	humidity = sense.get_humidity()

	threading.Timer(5, update_in_firebase).start()
	pi_ref.update({
		'environment': {'hum': humidity, 'pres': pressure, 'temp': temperature}
	})

update_in_firebase()
