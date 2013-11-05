if True:
    from settings import MIDDLEWARE_CLASSES
    
    if 'django.middleware.cache.UpdateCacheMiddleware' not in MIDDLEWARE_CLASSES:
        MIDDLEWARE_CLASSES.insert(0, 'django.middleware.cache.UpdateCacheMiddleware')
    if 'django.middleware.cache.FetchFromCacheMiddleware' not in MIDDLEWARE_CLASSES:
        MIDDLEWARE_CLASSES.append('django.middleware.cache.FetchFromCacheMiddleware')
    #print MIDDLEWARE_CLASSES
    
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }
    
    CACHE_MIDDLEWARE_KEY_PREFIX = "{{ project_name }}_"
    CACHE_MIDDLEWARE_SECONDS = 60
    try:
        from django.core.cache import cache
        cache.clear()
        print "cache cleared"
    except:
        print "problems clearing cache"

    print "cache settings imported"

