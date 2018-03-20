from logger import logger

class file_logger (logger):

	def __init__(self, log_level, file_name="file_log.txt"):
		logger.__init__(self, log_level)
		self.__file_name__ = file_name

	def log(self, log_level, message) :
		if (log_level <= self.__log_level__):
			my_file = open(self.__file_name__, "a")
			my_file.write("{}: {}\n".format(log_level, message))
			my_file.close()

