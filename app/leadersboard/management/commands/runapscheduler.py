import logging
from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from leadersboard.jobs.jobs import decide_winner, delete_old_job_executions

logger = logging.getLogger('jobs')

class Command(BaseCommand):
    help = 'Runs APScheduler.'

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone = settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), 'default')

        scheduler.add_job(
            decide_winner,
            trigger = CronTrigger(minute = '*/5'),  # Every 5 minutes
            id = 'decide_winner',
            max_instances = 1,
            replace_existing = True,
        )
        logger.info('Added job `decide_winner`.')

        scheduler.add_job(
            delete_old_job_executions,
            trigger = CronTrigger(day = '*/1'),  # Every day
            id = 'delete_old_job_executions',
            max_instances = 1,
            replace_existing=True,
        )
        logger.info('Added weekly job: `delete_old_job_executions`.')

        try:
            logger.info('Starting scheduler...')
            scheduler.start()
        except KeyboardInterrupt:
            logger.info('Stopping scheduler...')
            scheduler.shutdown()
            logger.info('Scheduler shut down successfully!')