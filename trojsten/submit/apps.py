from django.apps import AppConfig


class SubmitConfig(AppConfig):
    name = "trojsten.submit"
    label = "old_submit"
    verbose_name = "Submit"

    def ready(self):
        # This is here to register events.
        # See https://docs.djangoproject.com/en/2.2/topics/signals/#connecting-receiver-functions
        # For more information.
        import trojsten.submit.signals.notifications  # noqa
