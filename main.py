import os
import bitwarden
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def get_env(key: str):
    """
    Get an environment variable.
    """
    return os.getenv(key)

def load_page(driver: webdriver.Chrome, url: str):
    """
    Load a page in the browser.
    """
    driver.get(url)

def get_driver() -> webdriver.Chrome:
    """
    Get a driver for the Chrome browser.
    """
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def login(driver: webdriver.Chrome):
  """
  This function is responsible for logging in to the page.
  """
  page_url = get_env("PAGE_URL")
  master_password = get_env("BITWARDEN_MASTER_PASSWORD")

  if not page_url or not master_password:
    raise ValueError("PAGE_URL and BITWARDEN_MASTER_PASSWORD must be set")

  load_page(driver, page_url)

  session_token = bitwarden.unlock_vault(master_password)
  nfse_username, nfse_password = bitwarden.get_item(session_token, "www.nfse.gov.br")

  form_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'form'))
  )

  # Find the form and fill it out
  cnpj_input = form_element.find_element(By.ID, 'Inscricao')
  password_input = form_element.find_element(By.ID, 'Senha')
  hidden_input = form_element.find_element(By.NAME, '__RequestVerificationToken')

  cnpj_input.send_keys(nfse_username)
  password_input.send_keys(nfse_password)

  # Click the button
  submit_button = form_element.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
  submit_button.click()

  sleep(10)

def main() -> None:
  """
  This is the main function that will be used to run the script.
  The Script is responsbile to load the page and then find the form and fill it out.
  The form is responsible for my login credentials, then we create a new invoice NF-e.
  """

  driver = get_driver()
  login(driver)


if __name__ == "__main__":
    main()
