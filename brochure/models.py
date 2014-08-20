from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=20)
    tag_line = models.CharField(max_length=50)
    description = models.TextField()
    website = models.URLField(null=True)
    date_created = models.DateField()
    image = models.ImageField(upload_to='media', blank=True, null=True)
    LEVEL = (("Basic", "Basic"), ("Intermediate", "Intermediate"), ("Advanced", "Advanced"))
    level = models.CharField(max_length=12, choices=LEVEL, default="Basic")

    def __unicode__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=50)
    tag_line = models.CharField(max_length=50)
    abstract = models.TextField(null=True)
    body = models.TextField(null=True)
    date_created = models.DateField(null=True)
    image = models.ImageField(upload_to='media', blank=True, null=True)

    def __unicode__(self):
        return self.title

#
# class Image(models.Model):
#     image = models.ImageField(upload_to='media', blank=True, null=True)
#     project = models.ForeignKey(Project, related_name="image", null=True)
#     blog = models.ForeignKey(Blog, related_name="image", null=True)


class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    message = models.TextField()

    def __unicode__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=20)
    blog = models.ManyToManyField(Blog, related_name='tags')

    def __unicode__(self):
        return self.name