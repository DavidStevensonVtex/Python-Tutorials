# threading_timer.py
import threading
import time
import logging


def delayed():
    logging.debug("worker running")


logging.basicConfig(
    level=logging.DEBUG,
    format="(%(threadName)-10s) %(message)s",
)

t1 = threading.Timer(0.3, delayed)
t1.setName("t1")
t2 = threading.Timer(0.3, delayed)
t2.setName("t2")

logging.debug("starting timers")
t1.start()
t2.start()

logging.debug("waiting before canceling %s", t2.getName())
time.sleep(0.2)
logging.debug("canceling %s", t2.getName())
t2.cancel()
logging.debug("done")
