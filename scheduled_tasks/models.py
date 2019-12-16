import uuid 
from django.db import models
from croniter import croniter
# Create your models here.
from datetime import datetime

class SalesEmails(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.TextField()
    html_message = models.TextField()
    recepients = models.TextField()

    last_run_at = models.DateTimeField(null=True, blank=True)
    last_run_status = models.CharField(max_length=255)
    next_run_at = models.DateTimeField(null=True, blank=True)
    cron_expression = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        """
        function to evaluate "next_run_at" using the cron expression, so that it is updated once the report is sent.
        """
        self.last_run_at = datetime.now()
        iter = croniter(self.cron_expression, self.last_run_at)
        self.next_run_at = iter.get_next(datetime)
        super(SalesEmails, self).save(*args, **kwargs)

    class Meta:
        db_table = 'sales_emails'


