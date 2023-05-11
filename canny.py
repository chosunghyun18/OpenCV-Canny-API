from io import BytesIO

import numpy as np
import cv2
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route("/")
def test():
    return "Hello Flask!"

@app.route("/canny")
def do_canny():
    file = request.files.get('image_file', '')
    file_bytes = np.fromfile(file, np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny_img = cv2.Canny(gray_img, 100, 250)

    _, img_bin = cv2.imencode('.jpeg', canny_img)
    return send_file(
            BytesIO(img_bin),
            mimetype='image/png',
            as_attachment=True,
            download_name='edge.jpg')


if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8501")