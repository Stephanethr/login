from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_login = models.CharField(max_length=255)
    user_password = models.TextField()
    user_compte_id = models.IntegerField(unique=True)
    user_mail = models.EmailField(max_length=255)
    user_date_new = models.DateTimeField(auto_now_add=True)
    user_date_login = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.user_compte_id:  # Si user_compte_id n'est pas défini
            last_user = User.objects.all().order_by('user_compte_id').last()
            self.user_compte_id = last_user.user_compte_id + 1 if last_user else 1
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.user_login
