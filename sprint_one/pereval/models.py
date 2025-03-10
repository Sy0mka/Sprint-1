from django.db import models

class PerevalAdded(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('pending', 'В работе'),
        ('accepted', 'Принято'),
        ('rejected', 'Отклонено'),
    ]

    date_added = models.DateTimeField(auto_now_add=True)
    raw_data = models.JSONField()
    images = models.JSONField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')

    class Meta:
        db_table = 'pereval_added'

class PerevalAreas(models.Model):
    id_parent = models.BigIntegerField()
    title = models.TextField()

    class Meta:
        db_table = 'pereval_areas'

class PerevalImages(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    img = models.BinaryField()  # Для хранения bytea
    pereval = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE, related_name='pereval_images')

    class Meta:
        db_table = 'pereval_images'

class SprActivitiesTypes(models.Model):
    title = models.TextField()

    class Meta:
        db_table = 'spr_activities_types'