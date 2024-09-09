from behave import *
from features.pages.homepage import HomePage


@given(u'I got navigated to Home page')
def step_impl(context):
    context.check_page = HomePage(context.driver)
    assert context.check_page.my_page_check("Your Store")


@when(u'I enter valid product {product} into the Search box field')
def step_impl(context, product):
    context.check_page.search(product)


@when(u'I click on Search button')
def step_impl(context):
    context.search_page = context.check_page.search_button_click()


@then(u'Valid product should fet displayed in Search results')
def step_impl(context):
    assert context.search_page.search_result_displayed()


@when(u'I enter invalid product {product} into the Search box field')
def step_impl(context, product):
    context.check_page.search(product)


@then(u'Proper message should be displayed in Search results')
def step_impl(context):
    assert context.search_page.search_invalid_result_displayed("There is no product that matches the search criteria.")


@when(u'I do not enter anything into Search box field')
def step_impl(context):
    context.check_page.search('')
