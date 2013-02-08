from settings import INSTALLED_APPS, MIDDLEWARE_CLASSES, TEMPLATE_CONTEXT_PROCESSORS

INSTALLED_APPS += [
                   'cms',
                   'mptt',
                   'menus',
                   'sekizai',
                   ]

MIDDLEWARE_CLASSES += [
                       'cms.middleware.multilingual.MultilingualURLMiddleware',
                       'cms.middleware.page.CurrentPageMiddleware',
                       'cms.middleware.user.CurrentUserMiddleware',
                       'cms.middleware.toolbar.ToolbarMiddleware',
                       ]

TEMPLATE_CONTEXT_PROCESSORS += [
                                'cms.context_processors.media',
                                'sekizai.context_processors.sekizai',
                                ]

CMS_TEMPLATES = (
    ('index.html', 'Index'),
)