## 2024-06-24 - Accessible External Links in Gradio HTML
**Learning:** In Gradio `gr.HTML` components, external links must use `target="_blank"` and `rel="noopener noreferrer"` to ensure security and prevent app state loss. Additionally, "here" is an accessibility anti-pattern for link text; descriptive text should be wrapped in the anchor tag with an `aria-label` indicating it opens in a new tab.
**Action:** Always verify external links in `gr.HTML` have proper `target`, `rel`, and descriptive text/`aria-label` attributes.
