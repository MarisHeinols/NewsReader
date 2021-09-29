
from newsapi import NewsApiClient

from Logger import getLogger
from NewsGetter import getNews

logger = getLogger(__name__)

logger.info("Started")

## Getting news
getNews()

logger.info('Finished')




