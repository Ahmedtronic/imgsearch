from flask import Flask, jsonify
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


@app.route('/', methods=['POST'])
def index():
    image = Image.open("data/Screenshot 2023-04-13 at 7.31.33 PM.png")
    try:
        image.verify()
        print(str(image.filename))
        return str(image.filename)
    except Exception:
        return "None"

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
    


    
    
