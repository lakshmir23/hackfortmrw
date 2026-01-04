from playwright.sync_api import sync_playwright

def get_form_fields(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        labels = page.eval_on_selector_all(
            "label",
            "elements => elements.map(e => e.innerText)"
        )
        browser.close()
        return labels

def fill_field(url, field_label, value):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.get_by_label(field_label).fill(value)
        page.wait_for_timeout(2000)
