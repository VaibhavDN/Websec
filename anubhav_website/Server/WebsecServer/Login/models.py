from django.db import models

class UserDetails(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)

    def __str__(self):
        return "Username: " + self.username + " Password: " + self.password

class AdminDetails(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)

    def __str__(self):
        return "Username: " + self.username + " Password: " + self.password

class ModelsActiveStatus(models.Model):
    username = models.CharField(max_length = 30)
    statusString = models.CharField(max_length = 30)    #1 for active blocking 0 for inactive eg. 10111011. One bit for every model category.

    def __str__(self):
        return "Username: " + self.username + " StatusString: " + self.statusString