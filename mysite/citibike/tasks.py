from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from .utils import scrape_citibike_json

logger = get_task_logger(__name__)


# schedule scraper to run every ten minutes
@periodic_task(run_every=(crontab(minute="*/10")))
def scrape():
    logger.info("Start Citibike Scrape")
    result = scrape_citibike_json.scrape_json()
    logger.info("Task finished: result= %s" % result)
