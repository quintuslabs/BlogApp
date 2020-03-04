from django.db import models

class Article(models.Model):
  
    title = models.CharField(max_length = 100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    article_image = models.FileField(blank = True,null = True,upload_to='articles/')
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']