from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Set up the WebDriver
driver = webdriver.Chrome() # Use the appropriate driver for your browser

def test_home_page():
    try:
    
        # Open the home page
        driver.get("file:///A:/VII%20SEM/SELENIUM-PROJECT/index.html") 
    
        # Update the path to your index.html file
        driver.maximize_window()
    
        # Check if the homepage contains the logo "SkyFly"
        logo = driver.find_element(By.CLASS_NAME, "logo")
        assert logo.is_displayed(), "Logo is not displayed"
        print("Home page test passed: Logo is displayed")

        # Check if the "Home" link is active
        home_link = driver.find_element(By.LINK_TEXT, "Home")
        assert home_link.get_attribute("class") == "nav-link active", "Home link is not active"
        print("Home page test passed: 'Home' link is active")
    except Exception as e:
        print(f"Home page test failed: {e}")


def test_booking_page():
    try:
        
        # Navigate to the Booking page
        booking_link = driver.find_element(By.LINK_TEXT, "Booking")
        booking_link.click()
        time.sleep(2)

        # Fill out the booking form
        from_input = driver.find_element(By.ID, "from")
        from_input.send_keys("Mangalore")
        assert from_input.get_attribute("value") == "Mangalore", "From location is not correct"
        print("Booking page test passed: 'From' location is filled correctly")
        time.sleep(2)
        
        destination_input = driver.find_element(By.ID, "destination")
        destination_input.send_keys("New Delhi")
        assert destination_input.get_attribute("value") == "New Delhi", "Destination location is not correct"
        print("Booking page test passed: 'Destination' location is filled correctly")
        time.sleep(2)

        date_input = driver.find_element(By.ID, "date")
        date_input.send_keys("12-15-2024")
        assert date_input.get_attribute("value") == "2024-12-15", "Date is not correct"
        print("Booking page test passed: Date is filled correctly")
        time.sleep(2)

        passengers_input = driver.find_element(By.ID, "passengers")
        passengers_input.send_keys("2")
        assert passengers_input.get_attribute("value") == "2", "Number of passengers is not correct"
        print("Booking page test passed: Number of passengers is filled correctly")
        time.sleep(2)


        # Submit the form
        submit_button = driver.find_element(By.TAG_NAME, "button")
        submit_button.click()
        time.sleep(2)
    
        # Check if confirmation message is displayed
        confirmation_message = driver.find_element(By.ID, "confirmation-message")
        assert confirmation_message.is_displayed(), "Confirmation message is not displayed"
        print("Booking page test passed: Confirmation message is displayed")
        time.sleep(2)

        # Check if the confirmation message contains correct details
        from_location = driver.find_element(By.ID, "from-location")
        destination_location = driver.find_element(By.ID, "destination-location")
        booking_date = driver.find_element(By.ID, "booking-date")
        booking_passengers = driver.find_element(By.ID, "booking-passengers")
        
        assert from_location.text == "Mangalore", "Confirmation 'From' location is incorrect"
        assert destination_location.text == "New Delhi", "Confirmation 'Destination' location is incorrect"
        assert booking_date.text == "2024-12-15", "Confirmation date is incorrect"
        assert booking_passengers.text == "2", "Confirmation number of passengers is incorrect"
        print("Booking page test passed: Confirmation details are correct")
    except Exception as e:
        print(f"Booking page test failed: {e}")

def main():
    try:
        test_home_page()
        test_booking_page()
    finally:
        # Close the browser after the tests
        time.sleep(2)
        driver.quit()
        print("Test execution completed.")

if __name__ == "__main__":
    main()