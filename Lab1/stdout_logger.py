from logger import logger

class stdout_logger (logger):

	def log(self, log_level, message) :
		if (log_level <= self.__log_level__):
			print(str(log_level) + ': ' + message)
