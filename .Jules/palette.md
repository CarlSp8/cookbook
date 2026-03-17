# Palette Journal

## 2025-03-17 - Explicit instructions for implicit submissions
**Learning:** Gradio components using implicit submission mechanisms (like pressing Enter in a `.submit()` mapped `gr.Textbox`) often confuse users because there is no explicit button to click.
**Action:** Use the `info` parameter to explicitly instruct the user (e.g., `info="Press Enter to apply"`) when a component relies on `.submit()` to trigger an action.
