import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    """Fixture para configurar e iniciar a sessão do Appium para Android."""
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Android Emulator"
    options.app = "path/to/memp-demo-app.apk"  # Caminho simulado para o APK
    options.automation_name = "UiAutomator2"
    
    # Conexão com o servidor Appium local
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()

def test_add_product_to_cart(driver):
    """
    Teste automatizado: Valida a adição de um produto ao carrinho na Sauce Labs My Demo App.
    """
    wait = WebDriverWait(driver, 15)

    # Passo 1: Selecionar o primeiro produto do catálogo (usando accessibility_id padrão do app)
    product_card = wait.until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "product item"))
    )
    product_card.click()

    # Passo 2: Clicar no botão de adicionar ao carrinho
    add_to_cart_btn = wait.until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Tap to add product to cart"))
    )
    add_to_cart_btn.click()

    # Passo 3: Abrir o carrinho de compras
    cart_icon = wait.until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Displays number of items in cart"))
    )
    cart_icon.click()

    # Passo 4: Validar se o produto está presente na tela do carrinho
    cart_item = wait.until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "store item text"))
    )
    
    assert cart_item.is_displayed(), "O produto selecionado não foi encontrado no carrinho."