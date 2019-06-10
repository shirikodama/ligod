from django.db import models

class Gwave(models.Model):
    role = models.TextField()
    msg = models.TextField()
    gracedb_id = models.TextField(default='')
    received_at = models.IntegerField(default=0)
    exploded_at = models.IntegerField(default=0)
    alerttype = models.TextField(default='')
    id = models.IntegerField(primary_key=True)
