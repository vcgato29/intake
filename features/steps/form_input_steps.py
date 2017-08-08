from behave import when
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException



def fill_text_input(context, input_name, value):
    selector = 'input[name="{}"]'.format(input_name)
    element = context.browser.find_element_by_css_selector(selector)
    element.send_keys(value)


def click_submit_button(context, form_selector=''):
    selector = 'button[type="submit"]'
    if form_selector:
        selector = ' '.join([form_selector, selector])
    button = context.browser.find_element_by_css_selector(selector)
    button.click()


@when('I click the "{checkbox_name}" checkbox')
def click_single_option_checkbox(context, checkbox_name):
    selector = "input[name='{}']".format(checkbox_name)
    checkbox = context.browser.find_element_by_css_selector(selector)
    checkbox.click()


@when('"{checkbox_value}" is clicked on the "{checkbox_name}" radio button')
@when('the "{checkbox_name}" checkbox option "{checkbox_value}" is clicked')
def click_checkbox(context, checkbox_name, checkbox_value):
    selector = "input[name='{}'][value='{}']".format(
        checkbox_name, checkbox_value)
    checkbox = context.browser.find_element_by_css_selector(selector)
    checkbox.click()


@when('submit button in form "{form_class}" is clicked')
def click_submit(context, form_class):
    selector = "form.{} button[type='submit']".format(form_class)
    element = context.browser.find_element_by_css_selector(selector)
    element.click()


@when('I click the "{button_text}" submit button')
def click_submit_with_text(context, button_text):
    selector = "input[type='submit']"
    elements = context.browser.find_elements_by_css_selector(selector)
    matching_buttons = [
        element for element in elements
        if button_text == element.get_attribute('value')
    ]
    if len(matching_buttons) != 1:
        raise NoSuchElementException(
            str('Did not find one button with "{}". Found {} elements '
                'matching criteria').format(
                    button_text, len(matching_buttons)))
    matching_buttons[0].click()


@when('the "{input_name}" text input is set to "{value}"')
def type_in_textarea(context, input_name, value):
    selector = "input[name='{}'][type='text']".format(input_name)
    text = context.browser.find_element_by_css_selector(selector)
    text.send_keys(value)


@when('the "{input_name}" email input is set to "{value}"')
def type_in_email_input(context, input_name, value):
    selector = "input[name='{}'][type='email']".format(input_name)
    text = context.browser.find_element_by_css_selector(selector)
    text.send_keys(value)


@when('I select the "{option_name}" option for "{select_name}"')
def select_django_admin_related_option_by_name(
        context, select_name, option_name):
    selector = "select[name='{}'] option".format(select_name)
    option_elements = context.browser.find_elements_by_css_selector(selector)
    matching_options = [
        element for element in option_elements if
        option_name in element.text]
    if len(matching_options) != 1:
        raise NoSuchElementException(
            str('Did not find one option with text: "{}". Found {} elements '
                'matching criteria').format(
                    option_name, len(matching_options)))
    actionChains = ActionChains(context.browser)
    actionChains.double_click(matching_options[0]).perform()
