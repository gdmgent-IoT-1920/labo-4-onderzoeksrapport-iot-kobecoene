const dbConfig = {
    collection: 'raspberry',
    document: 'student pi'
};

const app = {
    init() {
        // initialiseer de firebase app
        firebase.initializeApp(firebaseConfig);
        this._db = firebase.firestore();
        // cache the DOM
        this.cacheDOMElements();
        this.cacheDOMEvents();

        this._matrix = {
            isOn: false, color: {value: '#000000', type: 'hex'}
        };
    },
    cacheDOMElements() {
        // for color matrix
        this.$colorPicker = document.querySelector('#colorPicker');
        this.$toggleMatrix = document.querySelector('#toggleMatrix');
        this.$btnChange = document.querySelector('#btnChange');

        let tempr = document.querySelector('.temperature');
        let press = document.querySelector('.pressure');
        let humi = document.querySelector('.humidity');

        console.log(tempr)

        let docRef = this._db.collection(dbConfig.collection).doc(dbConfig.document)

        docRef.onSnapshot(function(doc) {
            let hum = doc.data().environment.hum;
            let temp = doc.data().environment.temp;
            let pres = doc.data().environment.pres;
            
            tempr.innerHTML = temp;
            press.innerHTML = pres;
            humi.innerHTML = hum;
            
        });
    },

    cacheDOMEvents() {
        // for color matrix
        this.$btnChange.addEventListener('click', (e) => {
            e.preventDefault();
            this._matrix.color.value = this.$colorPicker.value;
            this._matrix.isOn = this.$toggleMatrix.checked;

            this.updateInFirebase();
        });
    },
    updateInFirebase() {
        // for color matrix
        this._db.collection(dbConfig.collection).doc(dbConfig.document)
            .set(
                {matrix: this._matrix},
                {merge: true}
            );
        
    }
}

app.init();