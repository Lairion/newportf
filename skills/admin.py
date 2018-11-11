from django.contrib import admin
from .models import CategoryOfSkills,Skill
# Register your models here.
class SkillInline(admin.TabularInline):
    model = Skill
    

class CategoryAdmin(admin.ModelAdmin):
    fields = ('name','slug',)
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name', )}
    inlines = [
    	SkillInline
    ]
admin.site.register(CategoryOfSkills, CategoryAdmin)

class SkillAdmin(admin.ModelAdmin):
    fields = ('name','slug','category')
    list_display = ['name']
admin.site.register(Skill, SkillAdmin)