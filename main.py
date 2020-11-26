from flask import Flask, render_template, url_for, redirect, request
from flask_cors import CORS, cross_origin
import qrcode
import base64
from io import BytesIO


app = Flask(__name__)
CORS(app)


beverage = ['pepsi', 'demisoda apple', 'georgia max', 'georgia original', 'hot six']


@app.route('/')
def index():
    return render_template('index.html', beverage=beverage)


@app.route('/order', methods=['POST'])
def order():
    beverage = request.form['beverages']
    room = request.form['room']
    data = {'beverage': beverage, 'label': room}
    
    img = qrcode.make(data)

    bufferd = BytesIO()
    img.save(bufferd, format="JPEG")
    image_string = base64.b64encode(bufferd.getvalue()).decode('utf-8')
    return render_template('showqr.html', img_data=image_string)
    



if __name__ == '__main__':
    app.run(debug=True)