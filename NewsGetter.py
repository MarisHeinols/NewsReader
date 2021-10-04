from newsapi import NewsApiClient
import pyttsx3
from Logger import getLogger
from ConfigReader import readConf
from datetime import date
from DataBase import addDataToMongo

# Get logger
logger = getLogger(__name__)
today = date.today()


def getNews():
    # Read configuartion file
    config = readConf()

    newsapi = NewsApiClient(api_key=config['api'])  # Setting the api key

    logger.info('Getting headlines from ' + config["selectedSources"])
    # Initalizing audio speaker and setting its volume
    engine = pyttsx3.init()
    engine.setProperty('volume', float(config["volume"]))
    engine.say('Getting latest headlines from ' + config["selectedSources"])
    # Getting top headlines from source
    top_headlines = newsapi.get_top_headlines(
        sources=config["selectedSources"])

    Headlines = top_headlines['articles']

    # Iterating trough headlines, printing and saying them outloud
    if Headlines:
        for aticle in Headlines:
            title = aticle['title']
            print(title)
            engine.say(title)
            addDataToMongo(title, config["selectedSources"],
                           today.strftime("%d/%m/%Y"))

    else:
        print("No headlines found!")
        engine.say("No headlines found!")
        logger.info(
            'There where no headlines with this source ' + config["selectedSources"])

    engine.say("End of news find out more at" + config["selectedSources"])

    engine.runAndWait()
