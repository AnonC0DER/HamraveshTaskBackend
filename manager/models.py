from django.db import models
from django.contrib.auth import get_user_model
from django_jalali.db import models as jmodels

class App(models.Model):
    '''
        App(s) model, contains main stuff, such as image, command, etc.
    '''
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    image = models.CharField(max_length=260)
    envs = models.JSONField(null=True, blank=True)
    command = models.CharField(max_length=360)
    created_at = jmodels.jDateTimeField('created at', auto_now_add=True)

    def __str__(self):
        return self.name


class Container(models.Model):
    '''
        Container(s) model, connects to an app.
        Each app can have multiple containers.
    '''
    class StatusChoices(models.TextChoices):
        RUNNING = 'R', 'Running'
        FINISHED = 'F', 'Finished'

    app = models.ForeignKey(App, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.FINISHED)
    created_at = jmodels.jDateTimeField('created at', auto_now_add=True)
    last_run = jmodels.jDateTimeField(auto_now=True)

    def __str__(self):
        return self.name