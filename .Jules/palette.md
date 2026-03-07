
## 2025-02-13 - Security and UX for External Links in Gradio
**Learning:** External links embedded in Gradio `gr.HTML` components must use `target="_blank"` and `rel="noopener noreferrer"` to ensure security and prevent navigating away from the app.
**Action:** Always add `target="_blank" rel="noopener noreferrer"` to anchor tags referencing external resources in Gradio HTML to prevent users from losing their application state.
