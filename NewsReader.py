from Logger import getLogger
from NewsGetter import getNews
from DataBase import createDb
from SetUp import packageSetUp

packageSetUp()

logger = getLogger(__name__)

createDb()

logger.info("Started")

# Getting news
getNews()


logger.info('Finished')
