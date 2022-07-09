from django.shortcuts import render
from portfolio import models


# Displays the mainpage for a portfolio
# Could be modified to support multiple users
def main_page(request):
    portfolio = models.Portfolio.objects.get(person_name="Brett Meirhofer")
    target_id = portfolio.id
    links = models.PortfolioLink.objects.filter(portfolio__pk=target_id)
    projects = models.Project.objects.filter(category__pk=request.GET.get('cat', 0))
    return render(request, "portfolio.html", {'portfolio': portfolio, 'projects': projects, 'links': links})


def view_project(request, target_id):
    portfolio = models.Portfolio.objects.get(person_name="Brett Meirhofer")
    project = models.Project.objects.get(id=target_id)
    skills = project.skills.all()
    images = models.ProjectImage.objects.filter(project__pk=target_id)
    features = models.Feature.objects.filter(project__pk=target_id).filter(current=True)
    p_features = models.Feature.objects.filter(project__pk=target_id).filter(current=False)
    links = models.ProjectLink.objects.filter(project__pk=target_id)
    return render(request, "project.html", {'portfolio': portfolio, 'project': project, 'skills': skills,
                                            'images': images, 'features': features, 'pfeatures': p_features,
                                            'links': links})
