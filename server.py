from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secrets make more secrets' 

@app.route('/')
def index():
    if 'visits' not in session:
        session['visits']=0
    session['visits']+=1
    session.modified = True
    return render_template("index.html")

@app.route('/add_visits')
def add_visits():
    session['visits']+=1
    return redirect('/')

@app.route('/destroy_session')
def detroy_session():
    session.pop('visits')
    session.modified = True
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)