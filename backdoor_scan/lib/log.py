import logging

# logger
formatter = logging.Formatter('[📅 %(asctime)s][💼%(levelname)s] 📝 %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
#logger = logging.getLogger("veinmind-sensitive")
logger = logging.getLogger("xApp-sensitive")
logger.setLevel(logging.INFO)  ## It just output basic info
logger.addHandler(handler)