from django.shortcuts import render, get_object_or_404
from .models import CategoryOfSkills,Skill
# Create your views here.
class SkillsViews(object):
    """docstring for SkillsViews"""
    @staticmethod
    def category_view(request,slug):
        category = get_object_or_404(CategoryOfSkills,slug=slug)
        context = {
            'category':category
        }
        return render(request,"category_view.html",context)

    @staticmethod
    def categories_view(request):
        categories = CategoryOfSkills.objects.all()
        context = {
            'categories':categories
        }
        return render(request,"categories_view.html",context)
