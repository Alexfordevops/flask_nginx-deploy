from flask import Flask, request , render_template 

app1 = Flask(__name__)

@app1.route('/')
def home():
    return '<h1>Homepage app1</h1>'
    
@app1.route('/salvador')
def salvador():
    return render_template('salvador.html')

@app1.route('/fortaleza')
def fortaleza():
    return render_template('fortaleza.html')
        
if __name__ == '__main__':
    app1.run(debug=True, host='0.0.0.0')
