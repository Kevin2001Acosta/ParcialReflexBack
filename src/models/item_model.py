from tortoise import fields, models

class Item(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField(null=True)
    
    class Meta:
        table = "items"