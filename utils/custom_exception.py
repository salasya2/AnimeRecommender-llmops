import sys

class CustomException(Exception):

    def __init__(self,message:str,error_detail:Exception = None):
        self.detailed_error_message = self.get_detailed_error(message,error_detail)
        super().__init__(self.detailed_error_message)
    
    @staticmethod
    def get_detailed_error(message, error_detail):
        _,_,exc_tb = sys.exc_info()
        filename = exc_tb.tb_frame.f_code.co_filename
        linenumber = exc_tb.tb_lineno
        return (

            f'{message} \n' 
            f'Error: {error_detail} \n'
            f'Filename : {filename} \n'
            f'Linenumber : {linenumber} \n'
        )
    
    def __str__(self):
        
        return self.detailed_error_message
