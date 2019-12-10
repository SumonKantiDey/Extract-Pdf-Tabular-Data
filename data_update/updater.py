from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from data_update import text_extract


def start():

    scheduler = BackgroundScheduler()
    scheduler.add_job(text_extract.read_data, 'interval', minutes=50)
    scheduler.start()
