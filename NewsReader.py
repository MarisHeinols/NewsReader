
from newsapi import NewsApiClient

from Logger import getLogger
from ConfigReader import readConf
from NewsGetter import getNews

logger = getLogger(__name__)

logger.info("Started")

## Getting news
getNews()

logger.info('Finished')




