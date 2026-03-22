
## 2025-02-19 - Explicit Guidance for Implicit Gradio Submissions
**Learning:** Gradio elements like `gr.Textbox` can trigger implicit `.submit()` actions (like pressing Enter), but these actions are not visually evident to users, potentially causing confusion, especially when these actions control the visibility of core components (like revealing a protected WebRTC interface).
**Action:** When a UI interaction relies on an implicit submission event to progress, explicitly communicate this requirement using the element's `info` parameter to improve discoverability and reduce friction. Also, external links inside `gr.HTML` elements should always contain `target="_blank"` and `rel="noopener noreferrer"` to keep the application state intact and ensure security.
