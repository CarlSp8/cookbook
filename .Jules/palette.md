## 2025-06-13 - Improved HTML Link Accessibility in Gradio
**Learning:** Gradio's `gr.HTML` components often lack standard accessibility features by default. Using descriptive link text (avoiding "here"), adding `target="_blank"`, `rel="noopener noreferrer"`, and an explicit `aria-label` is crucial for screen readers and security. Also, Gradio 6.0 changes default `padding` behavior, so explicitly setting `padding=True` prevents visual regressions.
**Action:** Always wrap descriptive text inside `<a>` tags and add a11y attributes when embedding custom HTML links in Gradio applications.
