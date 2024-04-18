import logging


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter(f'%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')

    file_handler = logging.FileHandler(f'logs/{name}.log', mode='w')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
