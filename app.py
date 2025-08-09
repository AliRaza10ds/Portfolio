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

if __name__=="__main__":
    from os import environ
    port=int(environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)