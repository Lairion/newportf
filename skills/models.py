from django.db import models

# Create your models here.
class CategoryOfSkills(models.Model):
    """
    Description: Model Description
    """
    name = models.CharField(max_length=200, db_index=True,verbose_name="Category name")
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Category of Skills"
        verbose_name_plural = 'Categories of Skills'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_of_skills', args=[self.slug])

# Create your models here.
class Skill(models.Model):
    """
    Description: Model Description
    """
    category = models.ForeignKey('CategoryOfSkills', on_delete=models.PROTECT, related_name='skills', verbose_name="Category of skills")
    name = models.CharField(max_length=200, db_index=True, verbose_name="Skill name")
    image = models.ImageField(upload_to='skill_logo/%Y/%m/%d/', blank=True, verbose_name="Skill logo")
    

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
