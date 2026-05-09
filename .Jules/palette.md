## 2025-02-28 - Gradio Implicit Submissions
**Learning:** Gradio textboxes with bound `.submit()` handlers do not visually indicate to the user that pressing 'Enter' will trigger an action. This is a critical UX trap for keyboard-driven interfaces, especially when the input hides itself upon submission.
**Action:** Always use the `info` parameter on `gr.Textbox` components to explicitly instruct users (e.g., "Press Enter to submit") when relying on `.submit()` events.
