from aws_helpers.ses import send_email
from scheduled_tasks.models import SalesEmails
from datetime import datetime
from celery import shared_task # notice the import of task and not shared task. 


@shared_task
def send_sales_emails():
    current_time = datetime.utcnow()
    scheduled_reports = SalesEmails.objects.filter(next_run_at__lt = current_time)
    for scheduled_report in scheduled_reports:
        scheduled_report.save()
        response = send_email(
            scheduled_report.recepients.split(","), 
            body=scheduled_report.html_message,
            subject=scheduled_report.subject
        )
        print(response)