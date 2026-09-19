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
    page.locator(".sidebar").hover()
    Vm = page.get_by_text("Vehicle Management",exact=True).click()
    page.get_by_role("button",name="Add Vehicle").click()
    vn = input("Enter Vehicle number: ")
    imei = input("Enter imei ")
    def add_details(vn,imei):
        page.get_by_placeholder("Enter Vehicle Number").fill(vn)
        page.get_by_text("Device Configures").click()
        page.locator('input[placeholder="Select IoT Devices"]').click()
        page.locator('[role="listbox"]').wait_for(state="visible")
        page.get_by_role("option", name="GPS Device", exact=True).click()
        page.get_by_placeholder("Enter IMEI Number").fill(imei)
        page.get_by_text("Driver Details", exact=True).click()
        page.get_by_role("button", name="Save Vehicle").click()
    add_details(vn, imei)
    input("Press Enter to close the browser...")
    browser.close()