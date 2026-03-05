## 2026-03-05 - Enhanced Gradio UI elements
**Learning:** Implicit submissions in Gradio components (like Textbox) can be unclear to users. Adding explicit helper text via the `info` parameter improves usability.
**Action:** Always add explicit helper text (e.g., `info="Press Enter..."`) to components that have an event listener bound to their `.submit()` method.
