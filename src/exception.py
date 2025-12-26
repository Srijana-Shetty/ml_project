# for exception handling purpose
import sys #any exception that is basically getting control the sys library will automatically have that information
import logging

#error_detail:sys , the error_detail is present inside sys
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()  #in which line or file the exception we are getting will be their in exc_info() which will be stored in exc_tb
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    
    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys ):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message







