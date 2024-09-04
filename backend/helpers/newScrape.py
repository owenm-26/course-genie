from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import requests
from dotenv import load_dotenv
import os 

def scraper():
    
    # Step 1: Set up Selenium with headless mode
    options = Options()
    options.add_argument('--headless=new')
    service = Service('/Users/owenmariani/Downloads/chromedriver-mac-arm64/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)

    def login():
        load_dotenv()
        username_str = os.getenv('BU_USERNAME')
        password_str = os.getenv('BU_PASSWORD')

        #enter username
        username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "j_username"))
    )
        username.send_keys(username_str)

        #enter password
        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "j_password"))
        )
        password.send_keys(password_str)

        #click login button
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "input-submit"))
        )
        button.click()
        return current_url
    
    def duo_mobile():
        #click login button
        print('******DUO MOBILE BLOCKED. Please open your app and approve.******')
        button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "trust-browser-button"))
        )
        button.click()
        print('Duo passed. Collecting data...')
         # Wait for the URL to change
        try:
            WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
        except:
            print("URL did not change within the expected time.")
        
    # Step 2: Automate login
    login_url = "https://shib.bu.edu/idp/"
    class_search_url="https://mybustudent.bu.edu/psp/BUPRD/EMPLOYEE/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_Main?"
    driver.get(class_search_url)
    current_url = driver.current_url
    if current_url.__contains__(login_url):
        current_url = login()

    # Wait for the URL to change
    try:
        WebDriverWait(driver, 10).until(EC.url_changes(current_url))
    except:
        print("URL did not change within the expected time.")

    # Check if you need Duo Mobile bot
    new_url = driver.current_url
    if new_url.__contains__('duosecurity'):
        duo_mobile()
    
    # Step 3: Extract cookies from the Selenium session
    cookies = driver.get_cookies()
    session_cookies = {cookie['name']: cookie['value'] for cookie in cookies}

    # Step 4: Use the cookies in requests
    api_url = "https://mybustudent.bu.edu/psc/BUPRD/EMPLOYEE/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=BU001&term=2248&date_from=&date_thru=&subject=&subject_like=&catalog_nbr=&start_time_equals=&start_time_ge=&end_time_equals=&end_time_le=&days=&campus=&location=&x_acad_career=&acad_group=BU1&rqmnt_designtn=&instruction_mode=&keyword=&class_nbr=&acad_org=&enrl_stat=O&crse_attr=&crse_attr_value=&instructor_name=&instr_first_name=&session_code=&units=&trigger_search="

    headers = {
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://mybustudent.bu.edu/psc/BUPRD/EMPLOYEE/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_Main?acad_group=BU1&enrl_stat=O',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'accept': 'application/json',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    def fetch_all_pages(api_url, headers, session_cookies):
        all_data = []
        page = 1
        while True:
            # Update the API URL with the current page number
            paged_url = api_url + f"&page={page}"
            print(f"Fetching page {page}...")

            # Send the request with cookies and headers
            response = requests.get(paged_url, headers=headers, cookies=session_cookies)
            
            if response == []:
                print(f"Failed to retrieve data for page {page}: {response.status_code}")
                break

            # Parse the JSON response
            data = response.json()

            if not data:  # If the data is empty, break the loop
                print(f"No more data available. Stopping at page {page}.")
                break
            
            # Append the current page's data to the all_data list
            all_data.extend(data)
            print(all_data[-1])
            
            # Check for a condition to stop the loop (if applicable)
            # If the API returns something indicating the last page, check for it here
            # Example: if data contains a 'has_more' field indicating more pages, you can check it.
            # if not data.get('has_more', True):
            #     break
            
            # Increment the page number
            page += 1
    
        return all_data

    # # Send the request with cookies and headers
    # response = requests.get(api_url, headers=headers, cookies=session_cookies)
    all_data = fetch_all_pages(api_url, headers, session_cookies)

    # Clean up
    driver.quit()

    # Step 5: Handle the response
    if all_data:
        print('Data scraped successfully')
        return {"status": 200, "body": all_data}
    else:
        print(f"Failed to retrieve data")
        return {"body": "Failed"}

if __name__ == "__main__":
    scraper()