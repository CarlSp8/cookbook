## 2025-05-18 - Improved Gradio Component Affordances
**Learning:** In Gradio, users might not know they need to press 'Enter' for Textboxes without explicit submit buttons, and simple dropdowns benefit from instructional text. Furthermore, HTML components in Gradio need `target="_blank"` and `rel="noopener noreferrer"` for external links to prevent users from accidentally navigating away from the web app state.
**Action:** Use the `info` parameter in Gradio components to provide clear usage instructions implicitly, and secure `gr.HTML` external links by default.
