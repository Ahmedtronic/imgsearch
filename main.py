from flask import Flask, jsonify
from flask import request
import os
from PIL import Image


app = Flask(__name__)


def is_valid_image(file):
    try:
        image = Image.open(file)
        image.verify()
        return True
    except:
        return False


@app.route('/', methods=['POST', "GET"])
def index():
    
    if request.method == 'POST':
        print("YES")
        image = request.files['fileup']
        newimage = Image.open(image)
        return jsonify({"Try": str(image.filename)})
    else:
        image = Image.open("data/Screenshot 2023-04-13 at 7.31.33 PM.png")
        counter = 0
        for file in os.listdir("data"):
            print("Hi)
            counter+=1
        try:
            image.verify()
            print(str(image.filename))
            return jsonify({"Choo Choo": str(image.filename) + str(counter)})
        except Exception:
            return "None"

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
    


    
    
