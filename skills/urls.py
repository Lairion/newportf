from django.urls import path
from .views import SkillsViews
urlpatterns = [
    path('skills_categories/<str:slug>', SkillsViews.category_view, name="skills_category"),
    path('skills_categories/',SkillsViews.categories_view,name='skills_categories')
]