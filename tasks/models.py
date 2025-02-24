from django.db import models


# Create your models here.
class Task(models.Model):
    project = models.ForeignKey("Project", null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)  # TextField doesn't use max_length
    due_date = models.DateField()  # Corrected typo from deu_date to due_date
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or "Untitled Task"


class TaskDetails(models.Model):
    PRIORITY_OPTIONS = (
        ('H', 'High'),
        ('L', 'Low'),
        ('M', 'Medium'),
    )
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name="details")
    assigned_to = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default='L')  # Default value set to 'L'

    def __str__(self):
        return f"{self.task.title} - {self.get_priority_display()}"


class Project(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()