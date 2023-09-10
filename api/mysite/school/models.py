from djongo import models


class School(models.Model):
    _id = models.ObjectIdField(primary_key=True, null=False, unique=True)
    name = models.CharField(max_length=300)

    class Meta:
        db_table = "schools"


