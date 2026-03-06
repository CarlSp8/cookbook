## 2025-03-06 - Gradio WebRTC Hidden Element Reveal Flow
**Learning:** Gradio UI logic relying entirely on `Textbox.submit()` (pressing Enter) lacks clear affordances for users because there's no visible submit button. When this flow triggers the revelation of complex hidden elements like WebRTC streams, users often stall.
**Action:** Always add the `info="Press Enter to submit"` parameter to `gr.Textbox` components that map to critical implicit submit events to improve UX and accessibility, especially when they act as the gatekeeper to the main UI.

## 2025-03-06 - Gradio External Links Security & UX
**Learning:** `gr.HTML` components with `<a>` tags in Gradio templates by default open links in the same tab, forcing users away from the WebRTC or streaming app state.
**Action:** Manually ensure all external `a href` links within `gr.HTML` have `target="_blank" rel="noopener noreferrer"` to prevent users from losing their session.
