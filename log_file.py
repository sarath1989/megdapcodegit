from logging.handlers import TimedRotatingFileHandler
import logging

# logger = logging.getLogger("Log")
# logger.setLevel(logging.INFO)
#
# fileFormat = logging.Formatter("%(asctime)s : %(levelname)s : %(filename)s : %(lineno)d  : %(message)s")
# logging.basicConfig()
logging.basicConfig(filename="logging_file.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)


