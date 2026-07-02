## 2025-03-09 - Accessible Links and State Preservation in Gradio
**Learning:** External links embedded in Gradio `gr.HTML` components without `target="_blank"` cause app state loss when clicked. Additionally, using "here" as link text is an accessibility anti-pattern that fails to provide context for screen readers.
**Action:** Always use `target="_blank"` and `rel="noopener noreferrer"` for external links in `gr.HTML`. Wrap descriptive text (e.g., "Get an API Key") inside the anchor tag instead of using "here", and provide an `aria-label` indicating it opens in a new tab.
