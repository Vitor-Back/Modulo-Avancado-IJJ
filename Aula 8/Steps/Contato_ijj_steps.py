from behave import given, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given(u'que estou na página de contato do Instituto Joga Junto')
def step_instituto_page(context):
    
    WebDriverWait(context.browser, 10).until(
        EC.title_contains("Instituto Joga Junto")
        )
    browser_title = context.browser.title
    assert 'Instituto Joga Junto' in browser_title, 'Título não encontrado'

@when(u'preencho o formulário de contato')
def input_form(context):
    context.browser.find_element(By.ID, 'nome').send_keys('Vitor')
    context.browser.find_element(By.ID, 'email').send_keys('Vitor.back10@outlook.com')
    context.browser.find_element(By.ID, 'mensagem').send_keys('Teste final - Baygon Quality')

    subject = context.browser.find_element(By.NAME, 'assunto')
    select_subject = Select(subject)
    select_subject.select_by_visible_text('Ser facilitador')

@when(u'envio o formulário')
def click_button(context):
    button_submit = context.browser.find_element(By.XPATH, "//*[@id='Contato']/div[1]/form/button")
    button_submit.submit()  

@then(u'os dados são recebidos com sucesso')
def step_imp(context):
    wait = WebDriverWait(context.browser, 10)
    alert = wait.until(EC.alert_is_present())
    assert 'Dados recebidos!' in alert.text
    alert.accept() 