from django.db import models
from tasks.models import Project, Task
from django.core.validators import MaxValueValidator, MinValueValidator

class BugReport(models.Model):
	project = models.ForeignKey(
		Project,
		related_name='BugReport',
		on_delete=models.CASCADE
	)
	title = models.CharField(max_length=100)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
 
	STATUS_BUGS = [
        ('Consideration', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено'),
    ]
	status = models.CharField(
        max_length=50,
        choices=STATUS_BUGS,
        default='New',
    )
	priority = models.IntegerField(
     	default=1,
		validators=[
			MinValueValidator(1),
			MaxValueValidator(5)
		]
    )
	
class FeatureRequest(models.Model):
	project = models.ForeignKey(
		Project,
		related_name='FeatureRequest',
		on_delete=models.CASCADE
	)
	title = models.CharField(max_length=100)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
 
	STATUS_BUGS = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]
	status = models.CharField(
        max_length=50,
        choices=STATUS_BUGS,
        default='New',
    )
	priority = models.IntegerField(
     	default=1,
		validators=[
			MinValueValidator(1),
			MaxValueValidator(5)
		]
    )