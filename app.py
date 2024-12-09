# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/hello', methods=['get'])
def hello():
    return"Olá, está é minha primeira API com Flask!"
if __name__=='__main__':
    app.run(debug=True)