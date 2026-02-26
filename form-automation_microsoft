import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def automate_with_detection():
    print("=== Form Automation - Microsoft ===")
    
    url = input("Form's url: ").strip()
    iterations = int(input("Iterations: "))
    
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    from webdriver_manager.chrome import ChromeDriverManager
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    for i in range(iterations):
        print(f"\nIteration {i+1}/{iterations}")
        driver.get(url)
        time.sleep(3)
        
        try:
            body = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Znajdź WSZYSTKIE interaktywne pola: radio, checkbox, textarea
            # Microsoft Forms często używa div z rolą 'radio' lub 'checkbox'
            all_interactive_elements = driver.find_elements(
                By.CSS_SELECTOR, "input[type='radio'], input[type='checkbox'], div[role='radio'], div[role='checkbox'], textarea, input[type='text']"
            )
            
            print(f"{len(all_interactive_elements)} interactive fields found.")
            
            for element in all_interactive_elements:
                try:
                    element.click()
                    time.sleep(0.2)
                    element.send_keys(Keys.SPACE)
                    time.sleep(0.2)
                except:
                    element.send_keys(Keys.SPACE)
                    time.sleep(0.2)
            
            for _ in range(len(all_interactive_elements)):
                body.send_keys(Keys.TAB)
                time.sleep(0.1)
            submit_buttons = driver.find_elements(
                By.XPATH, "//button[contains(., 'Submit') or contains(., 'Wyślij') or @type='submit']"
            )
            
            if submit_buttons:
                submit_buttons[0].click()
                print("  Submit clicked")
            else:
                body.send_keys(Keys.ENTER)
                print("  Form sent")
            
        except Exception as e:
            print(f"  Error, iteration: {i+1}: {e}")
        
        time.sleep(1)
    
    driver.quit()
    print("\n=== Finished ===")

if __name__ == "__main__":
    automate_with_detection()
