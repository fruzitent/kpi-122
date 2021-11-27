import logging


class Logger:
    def __init__(self, name):
        logging.basicConfig(
            level=logging.DEBUG,
            format="[%(asctime)s] [%(levelname)s] [%(name)s:%(lineno)d]: %(message)s",
        )

        self.stack_level = 3
        self.log = logging.getLogger(name)

    def debug(self, msg):
        self.log.debug(msg, stacklevel=self.stack_level)

    def info(self, msg):
        self.log.info(msg, stacklevel=self.stack_level)

    def warning(self, msg):
        self.log.warning(msg, stacklevel=self.stack_level)

    def error(self, msg):
        self.log.error(msg, stacklevel=self.stack_level, exc_info=msg)
