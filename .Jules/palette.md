## 2025-03-01 - External Links in Gradio HTML Components
**Learning:** External links embedded in Gradio `gr.HTML` components must use `target="_blank"` and `rel="noopener noreferrer"` to ensure security and prevent the user from navigating away, losing their app state. Additionally, using "here" as link text is an accessibility anti-pattern.
**Action:** When adding links in Gradio `gr.HTML`, always wrap descriptive text (e.g., "Get an API Key") inside the anchor tag rather than "here", and apply `target="_blank"` with an `aria-label` explicitly stating it opens in a new tab.
