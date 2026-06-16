## 2025-06-16 - External Links in Gradio HTML
**Learning:** External links embedded in Gradio `gr.HTML` components without `target="_blank"` and `rel="noopener noreferrer"` can cause app state loss and security risks, and using "here" for link text is an accessibility anti-pattern.
**Action:** Always wrap descriptive text inside anchor tags, add `aria-label` for new tabs, and ensure `target="_blank"` and `rel="noopener noreferrer"` are used for external links in Gradio.
