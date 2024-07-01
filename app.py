from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Dummy data for users
users = {
    'admin': 'adminpass',
    'doctor1': 'doctor1pass',
    'doctor2': 'doctor2pass'
}

# Dummy data for reports
reports = {
    'doctor1': 'reports/report1.txt',
    'doctor2': 'reports/report2.txt',
    'admin': 'reports/report3.txt'  # Admin can access all reports
}

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid credentials'
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    return render_template('doctor_dashboard.html', username=username, reports=reports)

@app.route('/report/<username>')
def report(username):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    # Read and display the report without proper backend validation
    with open(reports[username], 'r') as file:
        content = file.read()
    
    return render_template('report.html', content=content, requested_user=username)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
