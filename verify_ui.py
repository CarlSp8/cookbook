import os
import time
from playwright.sync_api import sync_playwright, expect

def run_test():
    with sync_playwright() as p:
        print("Launching browser...")
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        url = "http://127.0.0.1:7865"
        print(f"Navigating to {url}...")
        try:
            page.goto(url)
        except Exception as e:
            print(f"Failed to load page: {e}")
            exit(1)

        # Wait for load
        print("Waiting for heading...")
        try:
            expect(page.get_by_role("heading", name="Gen AI SDK Voice Chat")).to_be_visible(timeout=20000)
        except AssertionError:
            print("Timeout waiting for heading. taking screenshot...")
            page.screenshot(path="debug_timeout.png")
            raise

        # 1. Check link target
        print("Checking link attributes...")
        link = page.get_by_role("link", name="here")
        target = link.get_attribute("target")
        rel = link.get_attribute("rel")
        print(f"Link target: {target}, rel: {rel}")

        if target != "_blank":
            print(f"FAILED: Link target is {target}, expected '_blank'")
        if rel is None or "noopener" not in rel or "noreferrer" not in rel:
            print(f"FAILED: Link rel is {rel}, expected to contain 'noopener' and 'noreferrer'")

        # 2. Enter dummy API key
        print("Entering dummy API key...")
        # Note: Gradio inputs often have a label that Playwright can find
        # If get_by_label fails, we might need to be more specific
        api_input = page.get_by_label("API Key")
        api_input.fill("dummy_key")
        api_input.press("Enter")

        # 3. Wait for Voice dropdown
        print("Waiting for Voice dropdown...")

        # Wait a bit for the UI update
        time.sleep(2)

        voice_dropdown = page.get_by_label("Voice")
        expect(voice_dropdown).to_be_visible()

        # 4. Check for info text
        print("Checking for info text...")
        # The info text "Select the voice tone for Gemini" should be visible
        expect(page.get_by_text("Select the voice tone for Gemini")).to_be_visible()

        # 5. Take screenshot
        print("Taking screenshot...")
        page.screenshot(path="after_ux_improvements.png")
        print("Screenshot saved to after_ux_improvements.png")

        browser.close()

if __name__ == "__main__":
    run_test()
