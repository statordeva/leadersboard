import logging
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util
from leadersboard.models import User, Winner

logger = logging.getLogger('jobs')

def decide_winner():
    users = User.objects.order_by('-points').all()[:2]

    logger.info('Decide the winner...')

    if not users.exists():
        logger.info('No users to choose from.')
        return

    winner = False
    if users.count() < 2:
        winner = users[0]

    if users.count() == 2:
        if users[0].points > users[1].points:
            winner = users[0]

        if users[0].points < users[1].points:
            winner = users[1]

    if winner:
        Winner(user=winner, points=winner.points).save()
        logger.info('New winner: %s', winner.name)

    logger.info('...')
    return


# The `close_old_connections` decorator ensures that database connections, that have become
# unusable or are obsolete, are closed before and after your job has run. You should use it
# to wrap any jobs that you schedule that access the Django database in any way.
@util.close_old_connections
def delete_old_job_executions(max_age = 604_800):
    """
    This job deletes APScheduler job execution entries older than `max_age` from the database.
    It helps to prevent the database from filling up with old historical records that are no
    longer useful.

    :param max_age: The maximum length of time to retain historical job execution records.
                    Defaults to 7 days.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)