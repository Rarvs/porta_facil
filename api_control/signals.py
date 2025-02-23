from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.utils.timezone import now
import logging

logger = logging.getLogger(__name__)

def log_login(sender, request, user, **kwargs):
    logger.info(f"Usuário {user.username} fez login em {now()}")

def log_logout(sender, request, user, **kwargs):
    logger.info(f"Usuário {user.username} fez logout em {now()}")

user_logged_in.connect(log_login)
user_logged_out.connect(log_logout)
