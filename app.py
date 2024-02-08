from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verify the username and password (You can use PAM authentication here)
        if pam_auth(username, password):
            session['logged_in'] = True
            return redirect(url_for('create_user'))
        else:
            return 'Invalid credentials. Please try again.'

    return render_template('login.html')

def pam_auth(username, password):
    import pam
    pam_auth = pam.pam()
    return pam_auth.authenticate(username, password)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Call function to create user
        create_linux_user(username, password)
        return 'User created successfully!'
    return render_template('create_user.html')

def create_linux_user(username, password):
    import subprocess
    subprocess.run(['sudo', 'useradd', '-m', username])
    subprocess.run(['sudo', 'passwd', username], input=password.encode())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')
