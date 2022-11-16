from django.db import models
from django.contrib.auth import get_user_model
from django_jalali.db import models as jmodels
from simple_history.models import HistoricalRecords
from django.forms.models import model_to_dict

class App(models.Model):
    '''
        App(s) model, contains main stuff, such as image, command, etc.
    '''
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    image = models.CharField(max_length=260)
    envs = models.JSONField(null=True, blank=True)
    command = models.CharField(max_length=360)
    last_run = jmodels.jDateTimeField(null=True, blank=True)
    created_at = jmodels.jDateTimeField('created at', auto_now_add=True)
    history = HistoricalRecords()
    full_docker_command = models.CharField(max_length=360, null=True, blank=True, default=None)

    def __str__(self):
        return self.name

    @property
    def get_history(self):
        '''Used this property to solve "datetime is not JSON serializable" error'''
        results = [model_to_dict(history) for history in self.history.all()]
        histories = []
        for result in results:
            result['last_run'] = str(result['last_run'])
            
            histories.append(result)

        return histories


class Container(models.Model):
    '''
        Container(s) model, connects to an app.
        Each app can have multiple containers.
    '''
    class StatusChoices(models.TextChoices):
        RUNNING = 'running', 'Running'
        FINISHED = 'finished', 'Finished'

    app = models.ForeignKey(App, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.FINISHED)
    created_at = jmodels.jDateTimeField('created at', auto_now_add=True)

    def __str__(self):
        return self.name