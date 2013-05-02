from settings import INSTALLED_APPS, MIDDLEWARE_CLASSES, TEMPLATE_CONTEXT_PROCESSORS, STATIC_URL, gettext

INSTALLED_APPS += [
                   'cms',
                   'mptt',
                   'menus',
                   'sekizai',
                   ]

MIDDLEWARE_CLASSES += [
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

#UNCOMMENT TO USE LANGUAGES 
"""
CMS_LANGUAGES = {
        1: [
            {
                'code': 'en',
                'name': gettext(u'english'),
                'fallbacks': ['pt'],
                'public': True,
                'hide_untranslated': False,
                'redirect_on_fallback': False,
            },
            {
                'code': 'pt',
                'name': gettext(u'português'),
                'fallbacks': ['en'],
                'public': True,
            },
        ],
        2: [
            {
                'code': 'pt',
                'name': gettext(u'português'),
                'fallbacks': ['en'],
                'public': True,
            },
            {
                'code': 'en',
                'name': gettext(u'english'),
                'fallbacks': ['pt'],
                'public': True,
            },
        ],
        'default': {
            'fallbacks': ['pt', 'en'],
            'redirect_on_fallback': True,
            'public': False,
            'hide_untranslated': False,
        }
    }
"""