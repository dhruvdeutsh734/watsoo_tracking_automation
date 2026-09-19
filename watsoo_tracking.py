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
    Vm = page.get_by_text("Vehicle Management").click()
    input("Press Enter to close the browser...")
    browser.close()