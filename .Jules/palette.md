## 2025-04-28 - External Links in Gradio Apps Destroy State
**Learning:** External links inside Gradio `gr.HTML` components without `target="_blank"` cause the user to navigate away, completely losing their active session state (which is critical for apps requiring API keys or WebRTC connections).
**Action:** Always add `target="_blank"` and `rel="noopener noreferrer"` to external links in Gradio UIs, along with an `aria-label` like `(opens in a new tab)` for screen reader accessibility.
