from django.dispatch import receiver
from django.db.models.signals import pre_save
from manager.models import Container

@receiver(pre_save, sender=Container)
def set_docker_command(sender, instance, *args, **kwargs):
    '''
        This signal generates full docker command and set it to full_command field in App model, 
        Can be developed to use celery task and send this full_command to wherever it needed.

        example : docker run -e key1=value1 -e key2=value -l l1=v1 hub.hamdocker.ir/nginx:1.21 sleep 1000
    '''
    app = instance.app
    envs = app.envs
    
    if envs:
        envs = ''.join('-e {}={} '.format(key, value) for key, value in envs.items())
        full_docker_command = f'docker run {envs}-l l1=v1 {app.image} {app.command}'

    else:
        full_docker_command = f'docker run -l l1=v1 {app.image} {app.command}'
    
    app.full_docker_command = full_docker_command
    app.save()