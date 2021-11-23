from log.Logger import getLogger
from service.NewsGetter import getNews
from dataBase.DataBase import createDb
from service.SetUp import packageSetUp

packageSetUp()

logger = getLogger(__name__)

createDb()

logger.info("Started")

# Getting news
getNews()


logger.info('Finished')
