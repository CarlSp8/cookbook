## 2025-07-01 - Gradio HTML Link Accessibility
**Learning:** Using "here" for link text is an accessibility anti-pattern. Furthermore, external links embedded in Gradio `gr.HTML` components must use `target="_blank"` and `rel="noopener noreferrer"` to ensure security and prevent app state loss.
**Action:** Always wrap descriptive text (e.g., "Get an API Key") inside the anchor tag, and add an `aria-label` to indicate it opens in a new tab.
