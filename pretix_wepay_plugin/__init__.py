from django.utils.translation import gettext_lazy

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")

__version__ = "1.0.0"


class PluginApp(PluginConfig):
    name = "pretix_wepay_plugin"
    verbose_name = "WePay Plugin"

    class PretixPluginMeta:
        name = gettext_lazy("WePay Plugin")
        author = "Andreas Köckeis"
        description = gettext_lazy("Offer a WePay payment integration.")
        visible = True
        version = __version__
        category = "PAYMENT"
        compatibility = "pretix>=2.7.0"

    def ready(self):
        from . import signals  # NOQA


default_app_config = "pretix_wepay_plugin.PluginApp"
