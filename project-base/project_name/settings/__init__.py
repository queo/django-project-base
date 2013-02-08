from settings import *

# Import cms_settings
try:
    from cms_settings import *
except:
    pass

# import lcal_settings
try:
    from local_settings import *
except ImportError:
    pass
