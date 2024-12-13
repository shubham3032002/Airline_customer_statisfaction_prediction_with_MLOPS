from src.airline.exception import customException
from src.airline.logger import logging
import sys

def div(a,b):
    try:
        result=a/b
        logging.info("diving the number")
    except Exception as e:
        logging.error("error ocure")
        raise customException(e,sys)
    
    
    
if __name__ == "__main__":
    try:
        div(10,0)    
        
    except customException as ce:
        logging.error(str(ce)) 
        raise customException(ce,sys)
           