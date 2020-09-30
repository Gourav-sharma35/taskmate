from django.db import models
from django.contrib.auth.models import User

class TaskList(models.Model):
    manager=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    task=models.CharField(max_length=300)
    done=models.BooleanField(default=False)

def _str_(self):
    return self.task + "--" + self.done
