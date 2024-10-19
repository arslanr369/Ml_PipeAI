from flask import Flask
from src.logger import logging

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  # Corrected to 'methods'
def index():
    logging.info("We are testing our second method of logging")
    return "Welcome to Arsi ML project"

if __name__ == "__main__":
    app.run(debug=True)
