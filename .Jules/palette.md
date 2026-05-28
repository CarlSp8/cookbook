## 2025-05-15 - Gradio External Links State Loss
**Learning:** External links inside Gradio `gr.HTML` components without `target="_blank"` cause users to navigate away, completely destroying the single-page app state when they return. This is especially frustrating for users trying to fetch an API key mid-workflow.
**Action:** Always add `target="_blank"`, `rel="noopener noreferrer"`, and an `aria-label` indicating it opens in a new tab to any external links within Gradio HTML blocks to preserve app state and ensure screen reader accessibility.
