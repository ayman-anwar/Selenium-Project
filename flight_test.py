from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver
driver = webdriver.Chrome()

try:
    # Open the website
    driver.get("https://www.hianime.to")
    driver.maximize_window()
    time.sleep(3)

    # Locate the search bar
    search_bar = driver.find_element(By.NAME, "q")  # Update with the actual name or ID of the search bar
    search_bar.send_keys("One Piece")
    search_bar.send_keys(Keys.RETURN)
    time.sleep(5)

    # Validate the search results
    results = driver.find_elements(By.CSS_SELECTOR, ".result-title")  # Update with actual CSS selectors
    assert any("One Piece" in result.text for result in results), "Search results do not contain 'One Piece'."
    print("Test Passed: Search results are accurate.")

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    # Close the browser
    driver.quit()
