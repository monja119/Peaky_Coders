from django.db import models

# Create your models here.

class Users(models.Model):
    '''
        une table qui contient des infos des users
    '''
  
    frq = (
        ('1H', 'UNE HEURRE'), 
        ('1J', '1 JOUR'),
        ('2J','2 JOUR'),
        ('1S','UNE SEMAINE'),
    )
    
    user_email = models.CharField(max_length=25, blank=False)
    password = models.CharField(max_length=5, blank=False)
    email_password = models.CharField(max_length=30, blank=False)
    frequenceDeSuppression = models.CharField(max_length=2, choices=frq, blank=False)
    
    
    
    class Meta:
        verbose_name = ('User')
        verbose_name_plural = ('Users')
    
    def __str__(self) -> str:
        return self.name





