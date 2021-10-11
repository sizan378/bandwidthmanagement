from django.db import models
from django.contrib.auth.models import User 


class author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.FileField()
    details = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name.username

class category(models.Model):
    name = models.CharField(max_length = 150)
    

    def __str__(self):
        return self.name

class article(models.Model):
    article_author = models.ForeignKey(author, on_delete=models.CASCADE)
    pop_name = models.CharField(max_length = 150)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    Existing_Internet = models.IntegerField()
    Existing_Facebook = models.IntegerField()
    Existing_YouTube = models.IntegerField()
    Existing_BDInternet = models.IntegerField()
    
    Upgrade_Internet = models.IntegerField()
    Upgrade_Facebook = models.IntegerField()
    Upgrade_YouTube = models.IntegerField()
    Upgrade_BDInternet = models.IntegerField()

    

    data_show = models.BooleanField(default=False)
    

    add_date = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.pop_name

class upgrade(models.Model):
    post=models.ForeignKey(article, on_delete=models.CASCADE)
    upgrade_author = models.ForeignKey(author, on_delete=models.CASCADE)
    AfterUpgrade_Internet = models.IntegerField()
    AfterUpgrade_Facebook = models.IntegerField()
    AfterUpgrade_YouTube = models.IntegerField()
    AfterUpgrade_BDInternet = models.IntegerField()

    upgrade_date = models.DateField(auto_now=False, auto_now_add=True)
    




