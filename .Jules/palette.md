## 2024-05-10 - Gradio HTML Link State Loss
**Learning:** External links inside `gr.HTML` components in Gradio apps can cause users to accidentally navigate away and lose the web app state.
**Action:** Always use `target="_blank"` and `rel="noopener noreferrer"` along with an `aria-label` (e.g., "(opens in a new tab)") for external links in Gradio apps.
