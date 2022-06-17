# Import
from selenium import webdriver
import time
import os

# Interface with with driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Navigate to Parking Portal
driver.get("https://dotsumd.nupark.com/V2/Portal/Login?ReturnUrl=%2FV2%2FPortal")

# Login Credentials
username = ""
password = ""

# Car Information
license_plate = ""
year = ""

# Click login button
driver.find_element_by_id("UMD Login").click()

# Enter Username and Password and then press Login
driver.find_element_by_xpath(
    "/html/body/div[2]/div/div/div[1]/form/div[1]/input").send_keys(username)

driver.find_element_by_xpath(
    "/html/body/div[2]/div/div/div[1]/form/div[2]/input").send_keys(password)

driver.find_element_by_xpath(
    "/html/body/div[2]/div/div/div[1]/form/div[4]/button").click()
time.sleep(5)

# Exit Automatic Duo Push and Click Enter Passcode
time.sleep(3)
driver.switch_to.frame(0)
driver.find_element_by_xpath(
    "/html/body/div/div/div[4]/div/div/div/button").click()
time.sleep(3)
driver.find_element_by_xpath(
    "/html/body/div/div/div[1]/div/form/div[1]/fieldset/div[3]/button").click()
time.sleep(2)

# Extract Passcode from bypasscodes.txt


def generate_passcode():
    file_path = 'bypasscodes.txt'

    # check if size of file is 0. Terminate program if TRUE
    if os.stat(file_path).st_size == 0:
        print('No bypass codes are available')
        driver.close()
        exit()

    code = ""

    # Extract Code
    with open('bypasscodes.txt', 'r') as f:
        code = f.readlines()[-1]

    # Removes bypass code used from file
    fd = open("bypasscodes.txt", "r")
    d = fd.read()
    fd.close()
    m = d.split("\n")
    s = "\n".join(m[:-1])
    fd = open("bypasscodes.txt", "w+")
    for i in range(len(s)):
        fd.write(s[i])
    fd.close()

    # Confirmation of line deletion
    print("Last line of file deleted")
    # Check if new codes must be added
    if os.stat(file_path).st_size == 0:
        print("Must add new set of codes")

    # Display number of codes left
    file = open("bypasscodes.txt", "r")
    Counter = 0
    Content = file.read()
    CoList = Content.split("\n")
    for i in CoList:
        if i:
            Counter += 1

    print("You have", Counter, "codes left")

    # Send code
    return code


# Enter Passcode and login
passcode = generate_passcode()
driver.find_element_by_xpath(
    "/html/body/div/div/div[1]/div/form/div[1]/fieldset/div[3]/div/input").send_keys(passcode)
time.sleep(2)
driver.find_element_by_xpath(
    "/html/body/div/div/div[1]/div/form/div[1]/fieldset/div[3]/button").click()
driver.switch_to.default_content()
time.sleep(20)

##### Add vehicle to DOTS system #####
# Click add button
driver.find_element_by_xpath(
    "/html/body/div[3]/div/div/div/main/div/div/div/div/div[1]/scrollable-tabset/div/div[1]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/a[2]").click()
# Add License Plate
time.sleep(5)
driver.find_element_by_id("veh_license_plate").send_keys(license_plate)
time.sleep(3)
# Save
driver.find_element_by_id("saveButton").click()
time.sleep(5)

driver.close()
