## 2025-04-04 - Explicit Labels for Implicit Events
**Learning:** Implicit submission mechanisms (like pressing Enter in a `.submit()` mapped `gr.Textbox`) can be confusing. We should explicitly instruct the user (e.g., `info="Press Enter..."`). External links embedded in Gradio `gr.HTML` components must use `target="_blank"` and `rel="noopener noreferrer"` to ensure security and prevent users from accidentally navigating away from the web app state.
**Action:** Always add explicit info text for implicit submission and make external links open in new tabs.
