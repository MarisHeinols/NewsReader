from Logger import getLogger
import pip
logger = getLogger(__name__)

# Installing all the necessary packadges for programm


def packageSetUp():

    packages = ["newsapi-python", "pyttsx3", "datetime", "pymongo"]

    for package in packages:
        try:
            logger.info("Installing " + package + " package")
            __import__(package)
            logger.info(package + " Is already installed")
        except ImportError:
            pip.main(['install', package])
            logger.info(package + " Is installed successfully")
