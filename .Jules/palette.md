## 2025-02-26 - Gradio HTML Link Accessibility and State Preservation
**Learning:** External links embedded in Gradio `gr.HTML` components must use `target="_blank"` and `rel="noopener noreferrer"` to prevent app state loss when users click them. Additionally, using "here" as link text is an accessibility anti-pattern for screen readers.
**Action:** Always wrap descriptive text (e.g., "Get an API Key") inside the anchor tag, use `target="_blank"`, `rel="noopener noreferrer"`, and provide an `aria-label` indicating it opens in a new tab.
