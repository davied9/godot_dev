import logging


logger = logging.getLogger("godot_dev")
logger.level = logging.INFO
logger.addHandler(logging.StreamHandler())


def add_log_file(log_file_path, append=True):
    kwargs = { "filename" : log_file_path, "encoding" : "utf-8" }
    if append:
        kwargs["mode"] = "a"
    logger.addHandler(logging.FileHandler(**kwargs))


# tests
def test_add_log_file():
    add_log_file("a.log")
    add_log_file("b.log")
    for handler in logger.handlers:
        try:
            print("file : ", handler.baseFilename)
        except:
            pass
    print("n handlers : ", len(logger.handlers))

def test_logging():
    logger.error("test info")


if "__main__" == __name__:
    test_add_log_file()
    test_logging()

