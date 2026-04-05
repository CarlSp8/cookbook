## 2026-04-05 - Explicit submission instructions for Gradio components
**Learning:** Gradio components like `gr.Textbox` that rely on implicit `.submit()` events (like pressing Enter) can be confusing for users if the required interaction isn't clear, especially when they control visibility of core features like WebRTC.
**Action:** Always provide explicit instructions using the `info` parameter (e.g., `info="Press Enter to submit"`) when relying on implicit submission events to reveal hidden UI states.
