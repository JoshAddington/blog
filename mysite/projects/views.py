import requests
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from projects.models import Project
from projects.forms import ProjectForm


def project_list(request):
    projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'projects/project_list.html', {'projects': projects})


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    posts_length = len(project.post_set.all())
    return render(request, 'projects/project_detail.html', {'project': project, 'posts_length': posts_length})


@login_required
def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST or None, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            return redirect('projects.views.project_detail', slug=project.slug)
    else:
        form = ProjectForm()
    return render(request, 'projects/project_edit.html', {'form': form})


@login_required
def project_edit(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            return redirect('projects.views.project_detail', slug=project.slug)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/project_edit.html', {'form': form})


@login_required
def project_draft_list(request):
        projects = Project.objects.filter(published_date__isnull=True).order_by('created_date')
        return render(request, 'projects/project_draft_list.html', {'projects': projects})


@login_required
def project_publish(request, slug):
    project = get_object_or_404(Project, slug=slug)
    project.publish()
    return redirect('projects.views.project_detail', slug=slug)


@login_required
def project_delete(request, slug):
    project = get_object_or_404(Project, slug=slug)
    project.delete()
    return redirect('projects.views.project_list')


def get_boroughs():
    r = requests.get(
        "http://bl.ocks.org/phil-pedruco/raw/6646844/830fab4f3a9cb28766c292c10fd99837bfcd1b80/nyc.json"
    )
    data = json.loads(r.text)
    return data
