from django.conf import settings
from django.test import Client
from importlib import import_module


class ModifySessionMixin(object):
    client = Client()

    def create_session(self):
        session_engine = import_module(settings.SESSION_ENGINE)
        store = session_engine.SessionStore()
        store.save()
        self.client.cookies[settings.SESSION_COOKIE_NAME] = store.session_key
