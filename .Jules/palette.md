## 2024-05-26 - External Links in Gradio Apps
**Learning:** External links embedded within Gradio `gr.HTML` components cause users to navigate away from the single-page application state, resulting in loss of their current session/data when they click them.
**Action:** Always use `target="_blank"` and `rel="noopener noreferrer"` with a descriptive `aria-label` indicating it opens in a new tab for all external links in Gradio HTML components.
