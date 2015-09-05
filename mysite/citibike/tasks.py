from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from datetime import datetime
from .models import TaskHistory
from .utils import scrape_citibike_json

logger = get_task_logger(__name__)


# schedule scraper to run every ten minutes
@periodic_task(run_every=(crontab(minute="*/10")), ignore_result=True)
def scrape():
    logger.info("Start Citibike Scrape")
    now = datetime.now()
    date_now = now.strftime("%d-%m-%Y %H:%M:%S")
    result = scrape_citibike_json.scrape_json()
    name = "citibike_scraper"
    taskhistory = TaskHistory.objects.get_or_create(name=name)[0]
    taskhistory.history.update({date_now: result})
    taskhistory.save()
    logger.info("Task finished: result= %s" % result)
