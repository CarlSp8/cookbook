## 2025-04-13 - Secure External Links in Gradio HTML
**Learning:** External links embedded in Gradio `gr.HTML` components must explicitly use `target="_blank"` and `rel="noopener noreferrer"` to ensure security and prevent users from accidentally navigating away from the web app state, along with a descriptive `aria-label` for screen readers.
**Action:** Always add these attributes to external links in `gr.HTML` to improve security, usability, and accessibility.
