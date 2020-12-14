from django.db import models

# Create your models here.

### user unique info are stored into database
class userDetails(models.Model):
    main_tysinc_id = models.CharField(max_length=55)
    email=models.EmailField(max_length=256,unique=True)
    pdf_tysnic_id = models.CharField(max_length=55)
    created_at = models.CharField(max_length=256)

    def __str__(self):
        return self.email
    


