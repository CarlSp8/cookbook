# Palette's Journal

## 2023-11-20 - [Explicit Instructions for Implicit Gradio Actions]
**Learning:** In Gradio applications (especially WebRTC examples like `fastrtc_ui.py`), UI state progression sometimes relies on implicit user actions—such as pressing 'Enter' inside a `.submit()` mapped `gr.Textbox` rather than clicking an explicit "Submit" button. Users may stare at an input field (like an API Key prompt) confused about how to proceed.
**Action:** When an implicit action (like pressing Enter) is required to trigger a component's `.submit()` event, explicitly communicate this requirement using the component's `info` parameter (e.g., `info="Press Enter to submit"`). This reusable UX pattern ensures clarity and reduces interaction friction in this design system.
