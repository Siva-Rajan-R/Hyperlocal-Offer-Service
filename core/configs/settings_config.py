from ..settings import OfferSettings
from hyperlocal_platform.core.utils.settings_initializer import init_settings
from ..constants import ENV_PREFIX,SERVICE_NAME

SETTINGS:OfferSettings=init_settings(settings=OfferSettings,service_name=SERVICE_NAME,env_prefix=ENV_PREFIX)