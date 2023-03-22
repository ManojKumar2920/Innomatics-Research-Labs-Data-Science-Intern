from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'hello'

@app.route('/', methods=["GET", "POST"])
def index():
    if 'notes' not in session:
        session['notes'] = []

    if request.method == "POST":
        note = request.form.get('note')
        note_in =str(note).strip(' ')
        if len(note_in) !=0:
            note_list=session['notes']
            note_list.append(note_in)
            session['notes'] = note_list
            print(session)
            return redirect(url_for('index'))
                            
    return render_template("home.html", notes=session['notes'])

if __name__ == '__main__':
    app.run(debug=True)