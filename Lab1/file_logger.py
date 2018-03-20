from logger import logger

class file_logger (logger):

	def log(self, log_level, message) :
		if (log_level <= self.__log_level__):
			my_file = open("file_log.txt", "a")
			my_file.write("{}: {}\n".format(log_level, message))
			my_file.close()
