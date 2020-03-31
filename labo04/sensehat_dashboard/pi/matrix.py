from sense_hat import SenseHat
import firebase_admin
from firebase_admin import credentials, firestore

#constants
COLLECTION = 'raspberry'
DOCUMENT = 'student pi'

#firebase
cred = credentials.Certificate("./config/iotlabo03-firebase-adminsdk-2u6kd-7ad4e729f6.json")
firebase_admin.initialize_app(cred)

def hex_to_rgb(value):
	value = value.lstrip('#')
	lv = len(value)
	return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def update_sensehat(doc_snapshot, changes, read_time):
	for doc in doc_snapshot:
		doc_readable = doc.to_dict()
		print(doc_readable)

		color = pi_ref.get().to_dict()['matrix']['color']['value']
		rgb = hex_to_rgb(color)
		sense.clear(rgb)

# connect firestore
db = firestore.client()
pi_ref = db.collection(COLLECTION).document(DOCUMENT)
pi_watch = pi_ref.on_snapshot(update_sensehat)

#senseHat
sense = SenseHat()
sense.set_imu_config(False,False,False)
sense.clear()

while True:
	pass




