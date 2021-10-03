
from newsapi import NewsApiClient

from Logger import getLogger
from NewsGetter import getNews
from DataBase import createDb

createDb()

logger = getLogger(__name__)

logger.info("Started")

# Getting news
getNews()

logger.info('Finished')
