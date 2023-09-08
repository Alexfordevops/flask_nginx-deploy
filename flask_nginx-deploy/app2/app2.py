from flask import Flask, request , render_template 

app2 = Flask(__name__)

@app2.route('/')
def home():
    return '<h1>Homepage app2</h1>'
    
@app2.route('/salvador')
def salvador():
    return render_template('salvador.html')

@app2.route('/fortaleza')
def fortaleza():
    return render_template('fortaleza.html')
        
if __name__ == '__main__':
    app2.run(debug=True, host='0.0.0.0')
