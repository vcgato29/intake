import logging
from django.utils import timezone

"""
Tab separated? Space separated?
key=value key2="value2"
page_name="/url/"
https://docs.djangoproject.com/en/1.11/topics/logging/#making-logging-calls

Goals:
- everything that goes to mixpanel is logged to stdout
- we can add lots of properties on the fly easily to both mixpanel & std out
- easy to add new calls in the codebase

"""

logger = logging.getLogger(__name__)

timestamp_format = '%Y-%m-%d %H:%M:%S.%f'


def format_for_log(*args, **kwargs):
    formatted_key_values = [
        "{}={}".format(key, value) for key, value in kwargs.items()]
    return "\t".join([
        *args, *formatted_key_values])


def format_and_log(log_type, level='info', **data):
    """log string in format: <log_datetime> <level> <log_type>
    <unpacked kwargs in key=value format separated by tabs>
    """
    level = level.lower()
    formatted_log = format_for_log(
        timezone.now().strftime(timestamp_format), log_type, **data)
    log_method = getattr(logger, level)
    log_method(formatted_log)
