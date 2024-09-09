from behave import *
from features.pages.homepage import HomePage
from features.pages.registerpage import RegisterPage
from utilities.generator import email_generator


@given(u'I navigate to RegisterPage')
def step_impl(context):
    context.enter_register = HomePage(context.driver)
    context.register_user = context.enter_register.enter_to_register()


@when(u'I fill all fields')
def step_impl(context):
    for row in context.table:
        name = row['name' ]
        last_name = row['last_name' ]
        email = email_generator()
        phone = row['phone']
        password = row['password']
        password_confirm = row['password']
        context.register_user.register_user(name, last_name, email, phone, password, password_confirm)


@when(u'I click Continue button')
def step_impl(context):
    context.register_user.register_button_click()


@then(u'Account Should be created')
def step_impl(context):
    assert context.register_user.warinig_message("Your Account Has Been Created!")


@when(u'I fill all fields and enter duplicate email')
def step_impl(context):
    for row in context.table:
        name = row['name']
        last_name = row['last_name']
        email = 'peternsk@inbox.ru'
        phone = row['phone']
        password = row['password']
        password_confirm = row['password']
        context.register_user.register_user(name, last_name, email, phone, password, password_confirm)


@then(u'1Proper massage should be displayed')
def step_impl(context):
    context.register_user = RegisterPage(context.driver)
    assert context.register_user.warinig_message_duplicated_email("Warning: E-Mail Address is already registered!")


@when(u'I do not fill any fields')
def step_impl(context):
    name = ''
    last_name = ''
    email = ''
    phone = ''
    password = ''
    password_confirm = ''
    context.register_user.register_user(name, last_name, email, phone, password, password_confirm)


@then(u'2Proper massage should be displayed about empty fields')
def step_impl(context):
    assert context.register_user.warinig_message_empty_form('First Name must be between 1 and 32 characters!')
