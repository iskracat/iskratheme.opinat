from cgi import escape
from datetime import date
from urllib import unquote

from plone.memoize.view import memoize
from zope.component import getMultiAdapter
from zope.deprecation.deprecation import deprecate
from zope.interface import implements, alsoProvides
from zope.viewlet.interfaces import IViewlet
from plone.app.layout.viewlets.common import ViewletBase

from AccessControl import getSecurityManager
from Acquisition import aq_base, aq_inner
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.layout.viewlets.common import PathBarViewlet

from plone.app.layout.globals.interfaces import IViewView

class PathBarViewletOpinat(ViewletBase):
    index = ViewPageTemplateFile('path_bar_opinat.pt')

    def update(self):
        super(PathBarViewlet, self).update()

        self.is_rtl = self.portal_state.is_rtl()

        breadcrumbs_view = getMultiAdapter((self.context, self.request),
                                           name='breadcrumbs_view')
        self.breadcrumbs = breadcrumbs_view.breadcrumbs()