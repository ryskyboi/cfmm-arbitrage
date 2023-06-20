import logging

log = logging.getLogger("chain")
log.setLevel(logging.DEBUG)
log.handlers.clear()
_console = logging.StreamHandler()
_format = '%(asctime)s.%(msecs)03d %(pathname)s:%(lineno)d %(module)s.%(funcName)s %(threadName)s %(levelname)-8s %(message)s'
_formatter = logging.Formatter(_format, "%Y%m%d %H:%M:%S")
_console.setFormatter(_formatter)
log.addHandler(_console)