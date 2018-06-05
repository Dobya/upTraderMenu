from django import template
from menu.models import menu, menuItem
import re

register = template.Library()

def get_links(chat_string):
    pattern = '(https?:\/\/)?([\w\.]+)\.([a-z]{2,6}\.?)(\/[\w\.]*)*\/?$'
    return re.findall(pattern, chat_string)
# Draw menu based on current page url
def draw_menu(request):
    path = request.path
    urls = get_links(path)
    return
# Draw menu based on name
def draw_menu_by_name(name):
    menuItem.object.filter(menu__title=name)