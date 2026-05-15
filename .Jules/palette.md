## 2024-05-24 - Gradio Implicit Submission Patterns
**Learning:** Gradio Textbox components with `.submit()` event listeners lack visual cues that pressing 'Enter' triggers an action, which can confuse users expecting a submit button.
**Action:** Always use the `info` parameter (e.g., `info="Press Enter to submit"`) on inputs mapped to `.submit()` to explicitly instruct users, especially when the component handles critical flow steps like authentication.
