from logging.handlers import RotatingFileHandler
import logging
import os.path


def init_logger(logger_name="root", base_dir='', log_file_name=""):
    # LOG_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'
    formatter = logging.Formatter(LOG_FORMAT)
    log_file_name = "{}.log".format(logger_name) if not log_file_name else log_file_name

    handler_Console = logging.StreamHandler()
    handler_Console.setFormatter(formatter)
    handler_Console.setLevel(logging.DEBUG)

    if not base_dir:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(base_dir, log_file_name)
    handler_F = RotatingFileHandler(log_path, maxBytes=200 * 1024, backupCount=5)
    handler_F.setFormatter(formatter)
    handler_F.setLevel(logging.DEBUG)

    logger = logging.getLogger(logger_name)
    logger.addHandler(handler_Console)
    logger.addHandler(handler_F)
    logger.setLevel(logging.DEBUG)
    return logger


logger = init_logger("chase", log_file_name="chase.log")