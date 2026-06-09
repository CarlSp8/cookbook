## 2025-03-08 - Accessible External Links in Gradio HTML
**Learning:** External links embedded in Gradio `gr.HTML` components must use `target="_blank"` and `rel="noopener noreferrer"` to ensure security and prevent app state loss. Additionally, avoid accessibility anti-patterns like using "here" for link text.
**Action:** Wrap descriptive text (e.g., "Get an API Key") inside the anchor tag and provide an `aria-label` indicating it opens in a new tab.
