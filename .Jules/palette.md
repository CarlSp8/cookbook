## 2024-05-15 - Gradio External Link Accessibility
**Learning:** External links within Gradio `gr.HTML` components need explicit `target="_blank"` and `rel="noopener noreferrer"` to prevent app state loss, and must avoid the "click here" anti-pattern by wrapping descriptive text with appropriate `aria-label`s.
**Action:** Always ensure external links in Gradio apps use descriptive text (not "here"), include `target="_blank" rel="noopener noreferrer"`, and provide an `aria-label` indicating that it opens in a new tab.
