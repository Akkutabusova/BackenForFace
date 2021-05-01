from django.apps import AppConfig


class BackForFaceConfig(AppConfig):
    name = 'back_for_face'

    def ready(self):
        import back_for_face.signal