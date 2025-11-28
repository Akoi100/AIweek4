# Task 2: Automated Testing with Selenium
# Login Page Test Automation

"""
This script automates testing of a login page using Selenium WebDriver.
It tests both valid and invalid credential scenarios.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from datetime import datetime

class LoginPageTester:
    """
    Automated test suite for login page functionality.
    """
    
    def __init__(self, base_url="https://practicetestautomation.com/practice-test-login/"):
        """
        Initialize the test suite.
        
        Args:
            base_url (str): The URL of the login page to test
        """
        self.base_url = base_url
        self.driver = None
        self.test_results = []
        
    def setup(self):
        """Set up the WebDriver."""
        # Using Chrome driver (can be changed to Firefox, Edge, etc.)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in headless mode
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        try:
            self.driver = webdriver.Chrome(options=options)
            self.driver.implicitly_wait(10)
            print("✓ WebDriver initialized successfully")
        except Exception as e:
            print(f"✗ Failed to initialize WebDriver: {e}")
            print("Note: Ensure ChromeDriver is installed and in PATH")
            
    def teardown(self):
        """Clean up and close the browser."""
        if self.driver:
            self.driver.quit()
            print("✓ WebDriver closed")
    
    def test_valid_login(self):
        """
        Test Case 1: Valid Login Credentials
        Expected: User should be logged in successfully
        """
        test_name = "Valid Login Test"
        print(f"\n{'='*50}")
        print(f"Running: {test_name}")
        print(f"{'='*50}")
        
        try:
            # Navigate to login page
            self.driver.get(self.base_url)
            
            # Find username and password fields
            username_field = self.driver.find_element(By.ID, "username")
            password_field = self.driver.find_element(By.ID, "password")
            
            # Enter valid credentials
            username_field.send_keys("student")
            password_field.send_keys("Password123")
            
            # Click submit button
            submit_button = self.driver.find_element(By.ID, "submit")
            submit_button.click()
            
            # Wait for success message or redirect
            time.sleep(2)
            
            # Verify successful login
            try:
                success_element = self.driver.find_element(By.CLASS_NAME, "post-title")
                if "Logged In Successfully" in success_element.text:
                    print("✓ Test PASSED: Successfully logged in")
                    self.test_results.append({"test": test_name, "result": "PASS"})
                    return True
            except NoSuchElementException:
                print("✗ Test FAILED: Success message not found")
                self.test_results.append({"test": test_name, "result": "FAIL"})
                return False
                
        except Exception as e:
            print(f"✗ Test FAILED: {e}")
            self.test_results.append({"test": test_name, "result": "FAIL", "error": str(e)})
            return False
    
    def test_invalid_username(self):
        """
        Test Case 2: Invalid Username
        Expected: Error message should be displayed
        """
        test_name = "Invalid Username Test"
        print(f"\n{'='*50}")
        print(f"Running: {test_name}")
        print(f"{'='*50}")
        
        try:
            self.driver.get(self.base_url)
            
            username_field = self.driver.find_element(By.ID, "username")
            password_field = self.driver.find_element(By.ID, "password")
            
            # Enter invalid username
            username_field.send_keys("invaliduser")
            password_field.send_keys("Password123")
            
            submit_button = self.driver.find_element(By.ID, "submit")
            submit_button.click()
            
            time.sleep(2)
            
            # Check for error message
            try:
                error_element = self.driver.find_element(By.ID, "error")
                if "Your username is invalid" in error_element.text:
                    print("✓ Test PASSED: Error message displayed correctly")
                    self.test_results.append({"test": test_name, "result": "PASS"})
                    return True
            except NoSuchElementException:
                print("✗ Test FAILED: Error message not found")
                self.test_results.append({"test": test_name, "result": "FAIL"})
                return False
                
        except Exception as e:
            print(f"✗ Test FAILED: {e}")
            self.test_results.append({"test": test_name, "result": "FAIL", "error": str(e)})
            return False
    
    def test_invalid_password(self):
        """
        Test Case 3: Invalid Password
        Expected: Error message should be displayed
        """
        test_name = "Invalid Password Test"
        print(f"\n{'='*50}")
        print(f"Running: {test_name}")
        print(f"{'='*50}")
        
        try:
            self.driver.get(self.base_url)
            
            username_field = self.driver.find_element(By.ID, "username")
            password_field = self.driver.find_element(By.ID, "password")
            
            # Enter valid username but invalid password
            username_field.send_keys("student")
            password_field.send_keys("wrongpassword")
            
            submit_button = self.driver.find_element(By.ID, "submit")
            submit_button.click()
            
            time.sleep(2)
            
            # Check for error message
            try:
                error_element = self.driver.find_element(By.ID, "error")
                if "Your password is invalid" in error_element.text:
                    print("✓ Test PASSED: Error message displayed correctly")
                    self.test_results.append({"test": test_name, "result": "PASS"})
                    return True
            except NoSuchElementException:
                print("✗ Test FAILED: Error message not found")
                self.test_results.append({"test": test_name, "result": "FAIL"})
                return False
                
        except Exception as e:
            print(f"✗ Test FAILED: {e}")
            self.test_results.append({"test": test_name, "result": "FAIL", "error": str(e)})
            return False
    
    def test_empty_credentials(self):
        """
        Test Case 4: Empty Credentials
        Expected: Error or validation message
        """
        test_name = "Empty Credentials Test"
        print(f"\n{'='*50}")
        print(f"Running: {test_name}")
        print(f"{'='*50}")
        
        try:
            self.driver.get(self.base_url)
            
            # Click submit without entering credentials
            submit_button = self.driver.find_element(By.ID, "submit")
            submit_button.click()
            
            time.sleep(2)
            
            # Check if still on login page (validation should prevent submission)
            current_url = self.driver.current_url
            if "login" in current_url.lower():
                print("✓ Test PASSED: Form validation working")
                self.test_results.append({"test": test_name, "result": "PASS"})
                return True
            else:
                print("✗ Test FAILED: Form submitted with empty fields")
                self.test_results.append({"test": test_name, "result": "FAIL"})
                return False
                
        except Exception as e:
            print(f"✗ Test FAILED: {e}")
            self.test_results.append({"test": test_name, "result": "FAIL", "error": str(e)})
            return False
    
    def generate_report(self):
        """Generate and display test results summary."""
        print(f"\n{'='*50}")
        print("TEST RESULTS SUMMARY")
        print(f"{'='*50}")
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results if result["result"] == "PASS")
        failed_tests = total_tests - passed_tests
        
        print(f"Total Tests: {total_tests}")
        print(f"Passed: {passed_tests}")
        print(f"Failed: {failed_tests}")
        print(f"Success Rate: {(passed_tests/total_tests*100):.1f}%")
        
        print(f"\nDetailed Results:")
        for result in self.test_results:
            status = "✓" if result["result"] == "PASS" else "✗"
            print(f"{status} {result['test']}: {result['result']}")
    
    def run_all_tests(self):
        """Execute all test cases."""
        print("="*50)
        print("AUTOMATED LOGIN PAGE TEST SUITE")
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*50)
        
        self.setup()
        
        if self.driver:
            # Run all test cases
            self.test_valid_login()
            self.test_invalid_username()
            self.test_invalid_password()
            self.test_empty_credentials()
            
            # Generate report
            self.generate_report()
        else:
            print("Cannot run tests: WebDriver initialization failed")
        
        self.teardown()


if __name__ == "__main__":
    # Create tester instance and run all tests
    tester = LoginPageTester()
    tester.run_all_tests()
    
    print("\n" + "="*50)
    print("NOTE: This script requires Selenium and ChromeDriver")
    print("Install with: pip install selenium")
    print("Download ChromeDriver from: https://chromedriver.chromium.org/")
    print("="*50)
