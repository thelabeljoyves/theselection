from menus.base import Modifier
from menus.menu_pool import menu_pool

from cms.models import Page


class TheselectionMode(Modifier):
    """

    """
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        extension = Page.theselectionextension
        for node in nodes:
            try:
                page = Page.objects.get(pk=node.id)
                extensions = page.theselectionextension
                node.subtitle = extensions.subtitle
                node.backgroundcolor = extensions.backgroundcolor
            except:
                pass
        return nodes

menu_pool.register_modifier(TheselectionMode)
