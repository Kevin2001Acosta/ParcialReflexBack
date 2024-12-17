from tortoise import fields, models

class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, unique=True)
    phone = fields.CharField(max_length=25)
    department = fields.CharField(max_length=255)
    cc = fields.CharField(max_length=255)
    active = fields.BooleanField(default=True)   
    class Meta:
        table = "users"
        
#nombre, email, telefono, departamento, cc, active