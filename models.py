from django.db import models


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
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.image_name
