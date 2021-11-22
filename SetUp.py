import os
from Logger import getLogger
logger = getLogger(__name__)
# Installing all the necessary packages for programm


def packageSetUp():

    packages = ["newsapi-python", "pyttsx3", "datetime", "pymongo", "certifi"]

    for package in packages:
        try:
            logger.info("Installing " + package + " package")
            __import__(package)
            logger.info(package + " Is already installed")
        except ImportError:
            os.system('python -m pip install '+package)
            logger.info(package + " Is installed successfully")
