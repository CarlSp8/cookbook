# Palette's UX Journal

## 2025-05-15 - Gradio Implicit Submission Visibility
**Learning:** Components with mapped `.submit()` events lack inherent visual indicators for submission (like "Press Enter"). This makes it unclear how to trigger the action if no obvious button exists, leading to poor accessibility and UX.
**Action:** Always use the `info` parameter on `gr.Textbox` (or similar components) to provide explicit instructions (e.g., `info="Press Enter..."`) when an event listener is bound to `.submit()`.
