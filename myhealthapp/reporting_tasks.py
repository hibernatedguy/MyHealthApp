import requests

# from applications.profiles.models import *
# from applications.machines.models import *
# from applications.checkups.models import *
# from applications.common.models import *


from celery.decorators import periodic_task
from datetime import timedelta


@periodic_task(run_every=timedelta(seconds=2))
def send_reports_to_report_server():
    r = requests.get('http://127.0.0.1:8080/users/')
    print('STATS -->', r.status_code)
    return True
