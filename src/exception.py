import os


## Comment
def error_message_detail(error,error_detail:str):
    __,__,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message= "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
      file_name,exc_tb.tb_lineno,str(error)
      
    return error_message
    )
      

## Comment
class Customexception(Exception):
    def __init__(self,error_message,error_detail:str):
        self.error_message=error_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        self.error_message
          