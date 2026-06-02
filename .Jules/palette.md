## 2025-02-27 - Gradio SPA External Link State Loss
**Learning:** External links embedded in Gradio `gr.HTML` components cause the application state to be lost when clicked because it navigates away from the single-page app context.
**Action:** Always use `target="_blank"` and `rel="noopener noreferrer"` for external links in `gr.HTML` to prevent state loss, along with descriptive link text and `aria-label` indicating it opens in a new tab.
