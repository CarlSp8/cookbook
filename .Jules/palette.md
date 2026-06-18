## 2025-06-18 - Prevent Gradio State Loss via External Links
**Learning:** Gradio applications lose their entire generated state if external links in `gr.HTML` navigate the user away from the page.
**Action:** Always wrap descriptive text in `a` tags (avoiding "here") and enforce `target="_blank"` with `rel="noopener noreferrer"` for external links to preserve single-page app state securely.
