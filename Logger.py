import logging


def getLogger(name, log_config= None):
    
    ## Setting data and time format for logging
    timeFormat = ("%(asctime)s;%(levelname)s;%(message)s")
    dateFormat = ("%d %b %Y %H:%M:%S")
    
    ## Logger is configured
    logging.basicConfig(filename='log_file.log',
                        encoding='utf-8', level=logging.INFO, format=timeFormat,datefmt=dateFormat)
    
    ## Returning logger object
    return logging.getLogger(name)
    
