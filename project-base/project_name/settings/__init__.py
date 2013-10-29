from settings import *

# Import cms_settings
try:
    from cms_settings import *
except Exception as e:
    print '!!Error importing CMS Settings!!'
    print e

try:
    from controlpanel.settings import *
except Exception as e:
    print '!!Error importing Control Panel Settings!!'
    print e
# import local_settings
try:
    from local_settings import *
except Exception as e:
    print '!!Error importing Local Settings!!'
    print e


try:
    if MEMCACHE_ENABLED:
        try:
            from cache_settings import *
        except:
            print '!!Error importing cache_settings !!'
            print e
except:
    pass

