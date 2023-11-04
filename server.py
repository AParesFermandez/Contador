from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

@app.route('/')
def home():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1

    user_visits = session.get('user_visits', 0)
    session['user_visits'] = user_visits + 1

    return render_template('index.html', visits=session['visits'], user_visits=session['user_visits'])

@app.route('/destroy_session')
def destroy_session():
    session.pop('visits', None)
    return redirect('/')

@app.route('/increment', methods=['POST'])
def increment():
    if 'visits' in session:
        session['visits'] += 2
    else:
        session['visits'] = 2
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['visits'] = 0
    return redirect('/')

@app.route('/custom_increment', methods=['POST'])
def custom_increment():
    increment_value = int(request.form['increment'])
    if 'visits' in session:
        session['visits'] += increment_value
    else:
        session['visits'] = increment_value
    return redirect('/')


if __name__ == '__main__':
    app.run()
