import os, sys
from src.logger import logging

def error_message_detailed(error, error_detailed: sys):
    _, _, exc_tb = error_detailed.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = 'Error occurred in Python script: [{0}], line number: [{1}], error message: [{2}]'.format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    
    return error_message

class customException(Exception):
    def __init__(self, error, error_detailed: sys):
        super().__init__(str(error))
        self.error_message = error_message_detailed(error, error_detailed=error_detailed)

    def __str__(self):
        return self.error_message

if __name__ == "__main__": 
    try:
        a = 1 / 0

    except Exception as e:
        logging.info("Division error by zero")
        raise customException(e, sys)
