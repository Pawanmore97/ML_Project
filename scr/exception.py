import sys

def get_error_msg(error,error_details:sys):

    _,_,exc_tb =error_details.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_msg = """Error occured in python script name [{0}] line no [{1}] error message [{2}]""".format(file_name,exc_tb.tb_lineno,str(error))

    return error_msg

class CustomeException(Exception):

    def __init__(self,error,error_details:sys):
        super().__init__(error,error_details)
        self.error_msg = get_error_msg(error,error_details)

    def __str__(self):
        return self.error_msg