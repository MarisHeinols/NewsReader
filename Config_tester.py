import os
from newsapi import NewsApiClient
import certifi
import pymongo
from configparser import ConfigParser

print("Configuration file test")

# Testing if configuration file exists on disk in the current working directory
print("----------")
print("Checking if config file exists -->")
assert os.path.isfile("configure.txt") == True
print("OK")
print("----------")

# Opening the configuration file
config = ConfigParser()
config.read('configure.txt')

# Checking if all NEWS API  related config options are present in the config file
print("Checking if config has NEWS API related options -->")
assert config.has_option('API', 'selectedSources') == True
assert config.has_option('API', 'selectedCategory') == True
assert config.has_option('API', 'volume') == True
assert config.has_option('API', 'api') == True
print("OK")
print("----------")

# Checking if all MYSQL related config options are present in the config file
print("Checking if config has MONGO DB related options -->")
assert config.has_option('DB', 'user') == True
assert config.has_option('DB', 'password') == True
assert config.has_option('DB', 'dataBase') == True
print("OK")
print("----------")

# Checking if possible to connect to nasa with the existing config options
print("Checking if it is possible to connect to NEWS API with the given config options -->")
newsapi = NewsApiClient(api_key=config.get('API', 'api'))
top_headlines = newsapi.get_top_headlines(
    sources=config.get('API', 'selectedSources'))

Headlines = top_headlines['articles']
assert (len(Headlines) > 0) == True

print("OK")
print("----------")

# Checking if possible to connect to MongoDb with the existing config options
print("Checking if it is possible to connect to MongoDb with the given config options -->")
ca = certifi.where()
mongodb_user = config.get('DB', 'user')
mongodb_password = config.get('DB', 'password')
mongodb_database = config.get('DB', 'dataBase')
connection = pymongo.MongoClient(
    f'mongodb+srv://{mongodb_user}:{mongodb_password}@{mongodb_database}.ray5r.mongodb.net/{mongodb_database.capitalize()}?retryWrites=true&w=majority', tlsCAFile=ca)
serverData = connection.admin.command('ismaster')

assert serverData["ismaster"] == True

print("OK")
print("----------")

# Checking if log file exist
print("Checking if DB migration component log config file exists log_migrate_db.yaml -->")
assert os.path.isfile("log_file.log") == True
print("OK")
print("----------")

print("Configuration file test DONE -> ALL OK")
print("----------------------------------------")
