import sys
from src.logger import logging

def error_message_details(error, error_detail: sys):
    # Getting traceback info
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        super().__init__(str(error))
        # Use the actual exception object instead of error_message string
        self.error_message = error_message_details(error, error_detail)

    def __str__(self):
        return self.error_message

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    
    try:
        a = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        logging.info("Divide by zero error occurred")
        raise CustomException(e, sys)
