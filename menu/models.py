from django.db import models

# Create your models here.
class menuItem(models.Model):
    title = models.CharField(max_length=64, blank=False, null=True)
    url = models.CharField(max_length=128, blank=True, null=True)
    parent = models.ForeignKey('menu.menuItem', on_delete=models.SET_NULL, blank=True, null=True)
    solve_url = models.BooleanField(default=False, blank=True)
    menu = models.ForeignKey('menu.menu', blank=True, null=True)
    menu_name = models.CharField(max_length=128, blank=True, null=True) # Root menu name, need to realize drawing by teplate tag
    is_active = False

    def __str__(self):
        return self.title


class menu(models.Model):
    title = models.CharField(max_length=64, blank=False, null=True) # Menu title
    url = models.CharField(max_length=128, blank=True, null=True) # Menu url

    def __str__(self):
        return self.title
