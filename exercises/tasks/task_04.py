from exercises.tasks.resources.resource_03_04 import open_kiwi_website_and_accept_cookies


# Travel mode interactions are respected by the UI
def test_travel_mode_interactions_are_respected_by_the_ui(page):
    # 1. On the Kiwi.com website hit the travel mode button (which has the Return value selected by default)
    # 1.1. Open the kiwi.com website and accept cookies

    # 1.2. Hit the travel mode button
    page.locator("").click()

    # 2. Verify a popup with the following options is displayed: Return, One-way, Multi-city, and Nomad
    page.locator("").wait_for(state="")
    assert page.locator("").is_visible()  # the Return option is visible
    assert page.locator("").is_visible()  # the One-way option is visible
    assert page.locator("").is_visible()  # the Multi-city option is visible
    assert page.locator("").is_visible()  # the Nomad option is visible

    # 3. Select the One-way options
    page.locator("").click()

    # 4. Verify the One-way option is selected
    page.locator("").wait_for(state="")
    assert page.locator("").is_visible()

    # 5. Verify the Return date field is no longer displayed
    assert page.locator("").is_hidden()
