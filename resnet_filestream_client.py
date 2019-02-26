from __future__ import print_function

from PIL import Image
import flask
import io
import base64
import requests

from labels import labels

app = flask.Flask(__name__)

SERVER_URL = 'http://localhost:8501/v1/models/resnet:predict'


def predict_bytes(jpeg_bytes):

    predict_request = '{"instances" : [{"b64": "%s"}]}' % jpeg_bytes

    # Send few actual requests and report average latency.
    total_time = 0
    num_requests = 1  # 10
    for _ in range(num_requests):
        response = requests.post(SERVER_URL, data=predict_request)
        response.raise_for_status()
        total_time += response.elapsed.total_seconds()
        prediction = response.json()['predictions'][0]

    print('Prediction class: {}, avg latency: {} ms'.format(
        prediction['classes'], (total_time*1000)/num_requests))
    prob = prediction['probabilities'][prediction['classes']]
    return (prediction['classes'], prob)


@app.route("/predict", methods=["POST"])
def predict():
        # initialize the data dictionary that will be returned from the
        # view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            # read the image in PIL format
            image = flask.request.files["image"].read()
            jpeg_bytes = base64.b64encode(image).decode('utf-8')
            prediction = predict_bytes(jpeg_bytes)
            data["success"] = True
            data["label"] = labels[prediction[0]]
            data["prediction"] = prediction[0]
            data["confidence"] = prediction[1]
    # return the data dictionary as a JSON response

    return flask.jsonify(data)


if __name__ == "__main__":
    app.run()
