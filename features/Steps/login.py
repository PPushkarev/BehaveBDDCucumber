from behave import *
from features.pages.homepage import HomePage


@given(u'Login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_accunt()
    context.login_page= context.home_page.login_to_account()


@when(u'I enter valid email as {email} and valid password as {password} into fields')
def step_impl(context,email,password):
    context.login_page.enter_email(email)
    context.login_page.enter_password(password)


@when(u'I click on Login button')
def step_impl(context):
    context.account_page=context.login_page.login_button_click()


@then(u'I get logged')
def step_impl(context):
    assert context.account_page.check_account_enter()


@when(u'I enter invalid email {email} and valid password {password} into fields')
def step_impl(context, email, password):
    context.login_page.enter_email(email)
    context.login_page.enter_password(password)


@then(u'I get not  logged and get proper message')
def step_impl(context):
    assert context.login_page.wrong_login("Warning: No match for E-Mail Address and/or Password.")


@when(u'I enter valid email {email} and invalid password {password} into fields')
def step_impl(context, email, password):
    context.login_page.enter_email(email)
    context.login_page.enter_password(password)

@when(u'I enter invalid email {email} and invalid password {password} into fields')
def step_impl(context, email, password):
    context.login_page.enter_email(email)
    context.login_page.enter_password(password)


@when(u'I do not enter email and  password into fields')
def step_impl(context):
    context.login_page.enter_email('')
    context.login_page.enter_password('')
