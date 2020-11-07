import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import detector
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)
CORS(app)

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploader', methods = ['GET', 'POST'])
def upload():
    detected_file=detector.hash()
    print(detected_file)
    # if detected_file == '':
    #     return detected_file
    # else :
    return jsonify(detected_file)


if __name__ == '__main__':
   app.run(debug = True)