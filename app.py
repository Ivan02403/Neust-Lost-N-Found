from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
# app.secret_key = "super secret key"  # This line is commented out, which is fine if you don't need it.

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port="8080")  # Specify the port as "port=8080"
