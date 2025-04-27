from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"
    

class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=356)
    content = models.CharField(max_length=1000)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title} {self.content} {self.id}"
    

