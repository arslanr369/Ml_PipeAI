from flask import Flask
from src.logger import logging
from src.exception import customException
import os, sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  
def index():
    try:
        raise Exception("We are testing our custom exception handling")
    except Exception as e:
        # Corrected 'custmeException' to 'customException'
        abc = customException(e, sys)
        # Log the detailed error message
        logging.info(abc.error_message)
        return "Welcome to Arsi ML project"

if __name__ == "__main__":
    app.run(debug=True)
