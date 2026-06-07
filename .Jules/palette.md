## 2025-02-20 - Descriptive Link Text and Target Blank in Gradio HTML
**Learning:** Using "here" for link text is an accessibility anti-pattern. Furthermore, external links in Gradio `gr.HTML` components cause app state loss if they don't open in a new tab.
**Action:** Always wrap descriptive text inside the anchor tag, use `target="_blank"` and `rel="noopener noreferrer"`, and provide an `aria-label` indicating it opens in a new tab.
