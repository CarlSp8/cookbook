## 2024-05-23 - External Links in Gradio HTML
**Learning:** External links embedded within Gradio `gr.HTML` components lack automatic security and accessibility attributes (like `target="_blank"` and `aria-label`), which can lead users to accidentally navigate away from the app state and cause screen reader confusion.
**Action:** Always manually add `target="_blank"`, `rel="noopener noreferrer"`, and a descriptive `aria-label` to anchor tags in `gr.HTML` when linking externally.
