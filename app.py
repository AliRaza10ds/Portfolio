from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/resume')
def myreusme():
    return render_template('resume.html')

@app.route('/Projects')
def projects():
    return render_template('project.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/skills')
def skills():
    return render_template('skill.html')

app.run(debug=True)