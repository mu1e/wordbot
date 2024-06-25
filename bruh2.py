import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_syllable(driver):
    try:
        
        iframe = WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src='https://phoenix.jklm.fun/games/bombparty']")))
        
        
        syllable_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div")
        
        
        syllable_content = syllable_element.text.strip()
        
       
        driver.switch_to.default_content()
        
        return syllable_content
    except Exception as e:
        print(f"An error occurred while scraping the syllable content:", e)
        return None

def load_wordlist(file_path):
    with open(file_path, 'r') as file:
        return file.read().split()

def find_matching_words(wordlist, syllable):
    return [word for word in wordlist if syllable in word]

def main():
    previous_syllable = None
    wordlist = load_wordlist('wordlist.txt')
    
    try:
     
        driver = webdriver.Chrome()  
        driver.get("https://jklm.fun/")  
        time.sleep(3)  

        while True:
           
            current_syllable = scrape_syllable(driver)
            if current_syllable:
                if current_syllable != previous_syllable:
                    print(f"Syllable changed to: {current_syllable}")
                    previous_syllable = current_syllable
                    
                  
                    matching_words = find_matching_words(wordlist, current_syllable)
                    if matching_words:
                        random_word = random.choice(matching_words)
                        print("Matching word found:")
                        print(random_word)
                    else:
                        print("No matching words found.")
            
    except Exception as e:
        print("An error occurred:", e)
    finally:
        
        driver.quit()

if __name__ == "__main__":
    main()
