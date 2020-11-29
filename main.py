from flask import Flask, render_template, url_for, redirect, request
from flask_cors import CORS, cross_origin
import qrcode
import base64
from io import BytesIO


app = Flask(__name__)
CORS(app)


beverage = ['pepsi', 'demisoda apple', 'georgia max', 'georgia original', 'hot six']
pick = dict()

@app.route('/')
def index():
    return render_template('index.html', beverage=beverage)


@app.route('/order', methods=['POST'])
def order():
    
    global pick

    pick['beverage'] = request.form['beverages']
    pick['room'] = request.form['room']

   
    return redirect(url_for('showqr'))
    

@app.route('/showqr', methods=['GET'])
def showqr():

    data = pick
    img = qrcode.make(data)
    bufferd = BytesIO()
    img.save(bufferd, format="JPEG")

    image_string = base64.b64encode(bufferd.getvalue()).decode('utf-8')

    return render_template('showqr.html', img_data=image_string)




@app.route('/order', methods=['GET'])
def order2():

    return pick

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)