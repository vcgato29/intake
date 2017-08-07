from unittest.mock import patch
from behave import given, then
from project.services.logging_service import format_for_log


MOCK_LOG = None


@given('a log listener')
def patch_log_function(context):
    global MOCK_LOG
    log_patcher = patch('project.services.logging_service.format_and_log')
    MOCK_LOG = log_patcher.start()
    context.test.patches["log_patcher"] = log_patcher
    

@then('there should be a log that contains "{text}"')
def test_text_in_log_calls(context, text):
    """This does not include timestamping for the log, but is functional
    as a test for the body of the log"""
    if MOCK_LOG is None:
        raise Exception(
            'This step needs to be preceded by "Given a log listener"')
    formatted_log_calls = [
        format_for_log(*call_args, **call_kwargs)
        for name, call_args, call_kwargs in MOCK_LOG.mock_calls
    ]
    any_contains = any([
        text in formatted_log
        for formatted_log in formatted_log_calls])
    context.test.assertTrue(any_contains)