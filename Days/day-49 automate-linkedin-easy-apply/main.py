from selenium import webdriver; from selenium.webdriver.common.by import By; from selenium.webdriver.support.wait import WebDriverWait; from selenium.webdriver.support import expected_conditions as EC; from selenium.common.exceptions import StaleElementReferenceException; import config, time

DEBUG = True
successfully_applied_count = 0

def setup_driver():
    options = webdriver.ChromeOptions(); options.add_experimental_option('detach', True); 
    return webdriver.Chrome(options=options)

# //*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]


def main_sequence(driver):
    for _ in range(2): driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3848589350&f_AL=true&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R"); # looping this because sometimes it doesn't go to the right page and this seems to work

    log_in(driver)

    apply(driver)

    pause('end')

    driver.quit()


def pause(string=''):
    input(string)


def log_in(driver):
    try: WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'nav__button-secondary'))).click(); # find and click sign in button
    except: print('sign in button not found') if DEBUG else None; 

    driver.find_element(By.ID, 'username').send_keys(config.EMAIL); driver.find_element(By.ID, 'password').send_keys(config.PASSWORD);  # enter username and password into their inputs
    driver.find_element(By.CLASS_NAME, 'btn__primary--large').click() # click sign in button


def apply(driver):
    global successfully_applied_count
    apply_attempt_count = 0

    still_jobs_left = True

    while (still_jobs_left):
        try:
            try: WebDriverWait(driver, 5).until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, '.jobs-search-results__list-item a')) > 1); # wait until the jobs list container appears
            except: print('list of jobs not found') if DEBUG else None; 

            for e in driver.find_elements(By.CSS_SELECTOR, '.jobs-search-results__list-item a')[apply_attempt_count:]:
                e.click()

                time.sleep(0.5)

                # [successfully_applied_count].click() # click on the next job, using the applied to count to get the next index, might as wells

                # pause('here')

                driver.find_element(By.CLASS_NAME, 'jobs-apply-button').click() # click the easy apply button

                time.sleep(0.2)

                try: WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'artdeco-text-input--input'))).send_keys(config.PHONE_NUMBER); # find phone number entry and enter phone number
                except: print('phone number input not found') if DEBUG else None; 

                driver.find_element(By.XPATH, '//*[@aria-label="Continue to next step"]').click() # click next button

                time.sleep(0.2)

                driver.find_element(By.XPATH, '//*[@aria-label="Continue to next step"]').click() # click next button 

                time.sleep(0.2)

                for e in driver.find_elements(By.CLASS_NAME, 'artdeco-text-input--input'): e.send_keys('0'); 

                driver.find_element(By.XPATH, '//*[@aria-label="Review your application"]').click() # click review button 
                apply_attempt_count += 1
                print(apply_attempt_count)

                try: 
                    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Submit application"]'))); # find submit application button but don't click it
                    if DEBUG: print('simulating click event'); successfully_applied_count += 1; 
                except: print('submit application buttons not found, application rejected') if DEBUG else None; 

                driver.find_element(By.CLASS_NAME, 'artdeco-button').click() # click x button to quit application

                driver.find_element(By.XPATH, '//*[@data-control-name="discard_application_confirm_btn"]').click() # click discard button

                time.sleep(0.5)

        except StaleElementReferenceException:
            continue


if __name__ == '__main__':
    driver = setup_driver()
    main_sequence(driver)
