from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'supersecretkey123'  # WICHTIG: Für Sessions

# Login-Seite
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'test123':
            session['logged_in'] = True
            return redirect(url_for('startseite'))
        else:
            return "Login fehlgeschlagen – bitte zurück und erneut versuchen."
    return render_template('login.html')

# Root-Route leitet auf Login weiter
@app.route('/')
def root():
    return redirect(url_for('login'))

# Logout-Funktion (optional)
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

# Startseite – nur nach Login sichtbar
@app.route('/startseite')
def startseite():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('index.html')

# Login-Prüfung als Dekorator für alle geschützten Seiten
def login_required(f):
    def wrapper(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

@app.route('/selbstreflexion')
@login_required
def selbstreflexion():
    return render_template('selbstreflexion.html')

@app.route('/selbstreflexion-unterkategorien')
@login_required
def selbstreflexion_unterkategorien():
    return render_template('selbstreflexion - unterkategorien.html')

@app.route('/selbstreflexion-ich')
@login_required
def selbstreflexion_ich():
    return render_template('selbstreflexion-ich.html')

@app.route('/selbstreflexion-familie')
@login_required
def selbstreflexion_familie():
    return render_template('selbstreflexion-familie.html')

@app.route('/selbstreflexion-freunde')
@login_required
def selbstreflexion_freunde():
    return render_template('selbstreflexion-freunde.html')

@app.route('/selbstreflexion-lebensabschnitte')
@login_required
def selbstreflexion_lebensabschnitte():
    return render_template('selbstreflexion-lebensabschnitte.html')

@app.route('/tagebuch')
@login_required
def tagebuch():
    return render_template('Mein Tagebuch.html')

@app.route('/tipps')
@login_required
def tipps():
    return render_template('Tipps für Psychos.html')

@app.route('/achtsamkeit')
@login_required
def achtsamkeit():
    return render_template('achtsamkeit.html')

@app.route('/stressbewältigung')
@login_required
def stressbewältigung():
    return render_template('stressbewältigung.html')

@app.route('/meditation')
@login_required
def meditation():
    return render_template('meditation.html')

@app.route('/gesunder_schlaf')
@login_required
def gesunder_schlaf():
    return render_template('gesunder_schlaf.html')

@app.route('/psychotherapie-assistent')
@login_required
def psychotherapie_assistent():
    return render_template('formular.html')

@app.route('/submit', methods=['POST'])
@login_required
def submit():
    vorname = request.form['vorname']
    nachname = request.form['nachname']
    email = request.form['email']
    krankenkasse = request.form['krankenkasse']
    versichertennummer = request.form['versichertennummer']
    return redirect(url_for('danke'))

@app.route('/danke')
@login_required
def danke():
    return render_template('danke.html')

@app.route('/ergotherapie')
@login_required
def ergotherapie():
    return render_template('ergotherapie - unterkategorien.html')

@app.route('/spiel/gedaechtnis')
@login_required
def gedaechtnis_spiel():
    return render_template('gedaechtnis.html')

@app.route('/spiel/aufmerksamkeit')
@login_required
def aufmerksamkeit_spiel():
    return render_template('aufmerksamkeit.html')

@app.route('/spiel/logik')
@login_required
def logik_spiel():
    return render_template('logik.html')

@app.route('/spiel/sprache')
@login_required
def sprache_spiel():
    return render_template('sprache.html')

@app.route('/sozialarbeiter')
@login_required
def sozialarbeiter():
    return render_template('sozialarbeiter - unterkategorien.html')

if __name__ == '__main__':
    app.run(debug=True)
