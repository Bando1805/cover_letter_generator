# job_offer_linkedin.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class LinkedInDriver:

    def __init__(self):
        pass

    def login(self):
        # Creating an instance
        chrome_service = Service(executable_path="C:/Users/18gia/Documents/chromedriver.exe")
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")  # Add the headless argument
        
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)  # Pass the options to the webdriver
        
        # Logging into LinkedIn
        self.driver.get("https://linkedin.com/uas/login")

        # Wait for the username field to become visible
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))

        # Accepting cookies
        try:
            cookie_accept_button = self.driver.find_element(By.XPATH, "//button[contains(@class, 'artdeco-global-alert-action') and contains(@class, 'artdeco-button--primary') and contains(@action-type, 'ACCEPT')]")
            cookie_accept_button.click()
        except NoSuchElementException:
            print("Cookie accept button not found. Proceeding without accepting cookies.")

        # Inserting username and password
        username = self.driver.find_element(By.ID, "username")
        username.send_keys("stocks180599@gmail.com")  # Enter Your Email Address

        pword = self.driver.find_element(By.ID, "password")
        pword.send_keys("Calzino99")  # Enter Your Password

        # Click the submit button and wait for the homepage to load
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("https://www.linkedin.com/feed/"))

    def get_job_description(self, job_url):
        try:
            # Login to LinkedIn
            self.login()
            # Use the URL to navigate to the job post
            self.driver.get(job_url)

            # Wait for the job description element to become visible
            job_description_element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.ID, "job-details"))
            )

            # Extract the content of the job description
            job_description = ''
            job_description_rows = job_description_element.find_elements(By.XPATH, ".//span")  # Find all the child span elements

            for row in job_description_rows:
                if row.text.strip():
                    job_description += row.text.strip() + '\n\n'  # Add two newline characters after each row
            
            job_description = job_description.strip()  # Remove any leading or trailing whitespace
            job_description = ' '.join(job_description.split())  # Remove any extra whitespace between words
           
            return job_description

        except Exception as e:
            error_message = f"An error occurred while extracting the job description: {str(e)}"
            return error_message
