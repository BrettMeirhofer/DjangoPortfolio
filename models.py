from django.db import models
from django.utils.html import mark_safe
import os
import os.path
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


# Represents a user that has a portfolio
class Portfolio(models.Model):
    person_name = models.CharField(max_length=40)
    about_text = models.TextField()
    profile_image = models.ImageField(upload_to='images/portfolio/thumbs/', blank=True, null=True)
    background_image = models.ImageField(upload_to='images/portfolio/thumbs/', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.person_name


# Represents an external link for a portfolio
class PortfolioLink(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    link_name = models.CharField(max_length=50)
    link = models.URLField()

    def __str__(self):
        return self.link_name


# Represents a skill used in one or more projects
class Skill(models.Model):
    skill_name = models.CharField(max_length=40)

    def __str__(self):
        return self.skill_name


# Represents a project on the portfolio
class Project(models.Model):
    project_name = models.CharField(max_length=40)
    project_desc = models.TextField()
    skills = models.ManyToManyField(Skill)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    thumb = models.ImageField(upload_to='images/portfolio/thumbs/', blank=True, null=True)

    def __str__(self):
        return self.project_name


# Represents a feature or aspect that a project has implemented
class Feature(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=200)
    current = models.BooleanField()

    def __str__(self):
        return self.feature_name


# Represents an image demonstrating a project
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/portfolio/')
    thumb = models.ImageField(upload_to='images/portfolio/thumbs/', blank=True, null=True)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.image_name

    def image_tag(self):
        return mark_safe('<img src="/%s" width="150" height="150" />' % (self.image))

    def make_thumbnail(self):
        thumb_size = 160, 120
        image = Image.open(self.image)
        image.thumbnail(thumb_size, Image.ANTIALIAS)

        thumb_name = os.path.basename(self.image.name)
        thumb_extension = os.path.splitext(thumb_name)[1]
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False  # Unrecognized file type

        # Save thumbnail to in-memory file as StringIO
        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        # set save=False, otherwise it will run in an infinite loop
        self.thumb.save(thumb_filename, ContentFile(temp_thumb.read()))
        temp_thumb.close()

        return True


# Represents an external link for a project
class ProjectLink(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    link_name = models.CharField(max_length=50)
    link = models.URLField()

    def __str__(self):
        return self.link_name
