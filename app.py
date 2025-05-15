from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Dummy-Userdaten (für echtes Projekt: Datenbank!)
# users = {
#     "admin": "pass"
# }

# Startseite ohne Login
@app.route('/')
def index():
    return render_template('index.html')

# Login- und Registrierung entfernt

# Modul-Routen
@app.route('/selbstreflexion')
def selbstreflexion():
    return render_template('selbstreflexion.html')

@app.route('/selbstreflexion-unterkategorien')
def selbstreflexion_unterkategorien():
    return render_template('selbstreflexion - unterkategorien.html')

@app.route('/selbstreflexion-ich')
def selbstreflexion_ich():
    return render_template('selbstreflexion-ich.html')

@app.route('/selbstreflexion-familie')
def selbstreflexion_familie():
    return render_template('selbstreflexion-familie.html')

@app.route('/selbstreflexion-freunde')
def selbstreflexion_freunde():
    return render_template('selbstreflexion-freunde.html')

@app.route('/selbstreflexion-lebensabschnitte')
def selbstreflexion_lebensabschnitte():
    return render_template('selbstreflexion-lebensabschnitte.html')

@app.route('/tagebuch')
def tagebuch():
    return render_template('Mein Tagebuch.html')

@app.route('/tipps')
def tipps():
    return render_template('Tipps für Psychos.html')

@app.route('/achtsamkeit')
def achtsamkeit():
    return render_template('achtsamkeit.html')

@app.route('/stressbewältigung')
def stressbewältigung():
    return render_template('stressbewältigung.html')

@app.route('/meditation')
def meditation():
    return render_template('meditation.html')

@app.route('/gesunder_schlaf')
def gesunder_schlaf():
    return render_template('gesunder_schlaf.html')

@app.route('/psychotherapie-assistent')
def psychotherapie_assistent():
    return render_template('formular.html')

@app.route('/submit', methods=['POST'])
def submit():
    vorname = request.form['vorname']
    nachname = request.form['nachname']
    email = request.form['email']
    krankenkasse = request.form['krankenkasse']
    versichertennummer = request.form['versichertennummer']

    return redirect(url_for('danke'))

@app.route('/danke')
def danke():
    return render_template('danke.html')

@app.route('/ergotherapie')
def ergotherapie():
    return render_template('ergotherapie - unterkategorien.html')

@app.route('/spiel/gedaechtnis')
def gedaechtnis_spiel():
    return render_template('gedaechtnis.html')

@app.route('/spiel/aufmerksamkeit')
def aufmerksamkeit_spiel():
    return render_template('aufmerksamkeit.html')

@app.route('/spiel/logik')
def logik_spiel():
    return render_template('logik.html')

@app.route('/spiel/sprache')
def sprache_spiel():
    return render_template('sprache.html')

@app.route('/sozialarbeiter')
def sozialarbeiter():
    return render_template('sozialarbeiter - unterkategorien.html')

if __name__ == '__main__':
    app.run(debug=True)