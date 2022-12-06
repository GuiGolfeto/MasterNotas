# pysautogui Imports
from time import sleep
import pyautogui

from PySimpleGUI import PySimpleGUI as sg
import Ui.window as wd

# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#import variables
X1 = 1576
Y1 = 829

X2 = 494
Y2 = 883


def navegador(desc, price, ordem, NFremessa, NFretorno):
    nav = webdriver.Chrome()
    nav.maximize_window()

    # System login
    nav.get('http://138.0.140.51:5660/issweb/paginas/login;jsessionid=i7116Yt6Md6IPNX8AcxXFOMJ.undefined')
    sleep(1)
    nav.find_element(
        By.XPATH, '//*[@id="username"]').send_keys('34894404000198', Keys.TAB)
    sleep(2)
    nav.find_element(
        By.XPATH, '//*[@id="password"]').send_keys('Gui090503', Keys.ENTER)
    sleep(5)
    nav.find_element(By.XPATH, '//*[@id="navNfse"]/a').click()
    nav.find_element(By.XPATH, '//*[@id="j_idt88:layoutNfs"]').click()

    # Filling in NF data
    data = nav.find_element(
        By.XPATH, '//*[@id="formEmissaoNFConvencional:imDataEmissao_input"]').get_attribute('value')
    nav.find_element(
        By.XPATH, '//*[@id="formEmissaoNFConvencional:imDataCompetencia_input"]').send_keys(data)

    # CNAE activity
    drop = Select(nav.find_element(
        By.ID, 'formEmissaoNFConvencional:listaAtvCnae_input'))
    drop.select_by_visible_text(
        "4520001 - Serviços de manutenção e reparação mecânica de veículos automotores")
    nav.find_element(
        By.XPATH, '//*[@id="formEmissaoNFConvencional:listaAtvCnae_label"]').click()
    sleep(0.7)
    nav.find_element(
        By.XPATH, '//*[@id="formEmissaoNFConvencional:listaAtvCnae_label"]').click()

    # Municipal Activity
    drop2 = Select(nav.find_element(
        By.ID, 'formEmissaoNFConvencional:listaAtvAtd_input'))
    drop2.select_by_value('000014;0000001')
    sleep(2)

    # Services discrimination
    nav.find_element(
        By.XPATH, '//*[@id="formEmissaoNFConvencional:descricaoItem"]').send_keys(desc.upper())  # descrição
    sleep(2)
    nav.find_element(By.XPATH, '//*[@id="formEmissaoNFConvencional:vlrUnitario_input"]').send_keys(Keys.CONTROL,
                                                                                                   "a")  # valor
    nav.find_element(By.XPATH, '//*[@id="formEmissaoNFConvencional:vlrUnitario_input"]').send_keys(price,
                                                                                                   Keys.TAB)  # valor
    nav.find_element(
        By.XPATH, '//*[@id="formEmissaoNFConvencional:btnAddItem"]/span[2]').click()  # add desc
    sleep(2)

    # Comments
    pyautogui.scroll(-1000)
    pyautogui.click(x=X1, y=Y1)
    sleep(2)
    pyautogui.click(x=X2, y=Y2)
    sleep(3)
    pyautogui.click(x=X2, y=Y2)
    sleep(2)
    text_obs = f'documento referente a ordem de compra {ordem} nf de remessa {NFremessa} e nf de retorno de remessa {NFretorno} dados para deposito: banco bradesco agencia 020-5, conta corrente 3706-0'
    pyautogui.write(text_obs.upper())
    sleep(1)
    pop = sg.popup_ok('Verificação', 'Preencha o campo do CNPJ, lance e baixe a NF! ', 'Após isso clique em OK para lançar outra NF')
    
    if (pop == 'OK'):
        sleep(1)
        