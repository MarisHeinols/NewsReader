import re
import os.path
from Logger import getLogger

logger = getLogger(__name__)

def readConf():

    lines = []
    dict = {}
    ## Check if file exists

    if(os.path.exists('configure.txt')):

        with open('configure.txt') as conf:
            lines = conf.readlines()

    ## Spliting text in lines via regex

    for line in lines:
        values = line.split(":") 
        dict[values[0]] = values[1].strip() ## Values are adde to dictonary

    return dict
