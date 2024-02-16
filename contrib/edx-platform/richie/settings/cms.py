def plugin_settings(settings):
    """Common settings for Richie catalog connector"""
    settings.RICHIE_COURSE_HOOK = {
        "secret": "richiesecret",
        "sync_endpoint": "http://richie:8000/api/v1.0/course-runs-sync/",
        "create_endpoint": "http://richie:8000/api/v1.0/unesco-course-sync/",
        "timeout": 3,
    }
