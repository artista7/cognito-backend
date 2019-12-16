from rest_framework.serializers import *
from scheduled_tasks.models import SalesEmails

class SalesEmailsSerializer(ModelSerializer):
    class Meta:
        model = SalesEmails
        fields = ['id', 'subject', "html_message", 'recepients',
                  'last_run_at', "last_run_status",
                  'next_run_at', 'cron_expression']
        extra_kwargs = {
            "last_run_status": {"read_only": True}
        }

        


