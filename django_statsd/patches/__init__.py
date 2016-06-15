try:
    from django.utils.importlib import import_module
except ImportError:
    from importlib import import_module

from django.conf import settings

patches = getattr(settings, 'STATSD_PATCHES', [])

for patch in patches:
    import_module(patch).patch()
