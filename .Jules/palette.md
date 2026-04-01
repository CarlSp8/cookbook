
## 2025-02-28 - Secure external links and implicit submissions
**Learning:** External links in Gradio `gr.HTML` components must use `target="_blank"` and `rel="noopener noreferrer"` to prevent losing the web app state, and implicitly submitted Textboxes (like `api_key`) need `info` parameters explaining how to submit.
**Action:** Always add `target="_blank"` and `rel="noopener noreferrer"` to external links in `gr.HTML`, and explicit `info` instructions (e.g. "Press Enter...") to inputs with hidden `.submit()` handlers.
