import selenium
# from selenium.webdriver.chrome.options import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def add_numbers_to_whatsapp_group(numbers_file):
    # Create a ChromeOptions object and specify the profile to use.
    options = Options()
    options.add_argument("--profile-directory=Default")

    # Create a Chrome driver and open the WhatsApp web page.
    driver = webdriver.Chrome(options=options)
    driver.get("https://web.whatsapp.com/")

    # Find the group that you want to add the numbers to.
    group_name = "test_grp"
    group_element = driver.find_element_by_xpath(
        f"//span[@title='{group_name}']"
    )
    group_element.click()

    # Read the list of numbers from the CSV file.
    numbers_file = 'C:\\Users\\ASUS\\Desktop\\flipkart\\numbers.csv'
    with open(numbers_file, "r") as f:
        numbers = []
        for line in f:
            numbers.append(line.strip())

    # For each number, click on the "Add contact" button and enter the number.
    for number in numbers:
        contact_element = driver.find_element_by_xpath(
            f"//input[@placeholder='Search or start new chat']"
        )
        contact_element.send_keys(number)
        contact_element.send_keys(Keys.ENTER)

        # Click on the "Add contact" button.
        add_contact_button = driver.find_element_by_xpath(
            f"//button[@data-icon='add']"
        )
        add_contact_button.click()

    driver.close()

if __name__ == "__main__":
    numbers_file = "numbers.csv"
    add_numbers_to_whatsapp_group(numbers_file)
