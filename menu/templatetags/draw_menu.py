from django import template
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import resolve
from menu.models import menu, menuItem
import re

register = template.Library()

def get_links(chat_string):
    pattern = '(https?:\/\/)?([\w\.]+)\.([a-z]{2,6}\.?)(\/[\w\.]*)*\/?$'
    return re.findall(pattern, chat_string)
'''
@register.tag(name="draw_menu")
def draw_menu(parcer, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, menu_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
    if not (menu_name[0] == menu_name[-1] and menu_name[0] in ('"', "'")):
        raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
    return MenuDrawer(menu_name[1:-1])

class MenuDrawer(template.Node):
    def __init__(self, name):
        self.name = name
    def render(self, context):
        name = self.name
        items = menuItem.objects.filter(menu_name=self.name)
        path = context['path']
        active = get_active_url(path, items)
        levels = get_visible_items(active, items)
        print(context['request'])
        t = template.loader.get_template('menu/includes/menu.html')
        #return t.render(context({'menu': levels, 'active': active}, autoescape=context.autoescape))
        #return render(context['request'], 'menu/includes/menu.html', {'menu': levels, 'active': active}
        return levels
'''
@register.inclusion_tag('menu/includes/menu.html', takes_context=True, name='draw_menu')
def draw_menu_by_name(context, name):
    items = menuItem.objects.filter(menu_name=name)
    path = context['path']
    active = get_active_url(path, items)
    levels = get_visible_items(active, items)
    print(context['request'])
    return {'menu': levels, 'active': active}

def get_active_url(path, objects):
    #active = objects.get(url=path)
    #print(active)
    try:
        active = objects.get(url=path)
    except ObjectDoesNotExist:
        try:
            named_url = resolve(path).url_name
            active = objects.get(url=named_url)
        except:
            active = None
    finally:
        if not active is None:
            active.is_active = True
        return active
# Get the list of visible items by levels
def get_visible_items(active_item, objects):
    levels = []
    try:
        root_menu_item = objects.get(parent=None) # Get item without parent as a menu root.
    except ObjectDoesNotExist:
        return []
    parent = active_item
    while parent:
        levels.append(objects.filter(parent=parent))
        parent = parent.parent
    levels.append([root_menu_item,])
    return list(reversed(levels))