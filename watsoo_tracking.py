from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://aisadmin.watsoo.com/")
    Username = "aisadmin@watsoo.com"
    password = "Admin@2023#"
    def Login(Username, password):
        page.get_by_placeholder("you@company.com").fill(Username)
        page.get_by_placeholder("Enter your password").fill(password)
        page.get_by_role("button", name= "Sign In").click()
    Login(Username, password)

   
    vn = input("Enter Vehicle number: ")
    imei = input("Enter imei ")

    def add_details(vn,imei):
        page.locator(".sidebar").hover()
        page.get_by_text("Vehicle Management",exact=True).click()
        page.get_by_role("button",name="Add Vehicle").click()
        page.get_by_placeholder("Enter Vehicle Number").fill(vn)
        page.get_by_text("Device Configures").click()
        page.locator('input[placeholder="Select IoT Devices"]').click()
        page.locator('[role="listbox"]').wait_for(state="visible")
        page.get_by_role("option", name="GPS Device", exact=True).click()
        page.get_by_placeholder("Enter IMEI Number").fill(imei)
        page.get_by_text("Driver Details", exact=True).click()
        page.get_by_role("button", name="Save Vehicle").click()
    add_details(vn, imei)
    Name = input("Enter Dealer Name:")
    Email = input("Enter Dealer Email:")
    Phone_number = input("Enter Dealer Phone Number:")
    def user_add(Name,Email,Phone_number):
        page.locator(".sidebar").hover()
        page.get_by_text("User Management", exact=True).click()
        page.get_by_text("Dealer Management", exact=True).click()
        page.get_by_role("button", name = "Add Dealer").click()
        page.get_by_placeholder("Enter Name").fill(Name)
        page.get_by_placeholder("Enter Email").fill(Email)
        page.get_by_placeholder("Enter Phone").fill(Phone_number)
        page.get_by_placeholder("Official Email").fill(Email)
    user_add(Name,Email,Phone_number)

    input("Press Enter to close the browser...")
    browser.close()