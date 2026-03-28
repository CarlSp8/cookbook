## 2024-05-14 - Gradio Form Submissions and External Links
**Learning:** In Gradio, implicit form submissions via the Enter key (using `.submit()`) are not obvious to users. Adding `info="Press Enter to submit"` provides a necessary UX cue. Additionally, external links should always include `target="_blank" rel="noopener noreferrer"` for security and to prevent users from navigating away from the app.
**Action:** Always include an `info` instruction on `gr.Textbox` when it acts as the primary submission trigger, and secure external links with `target="_blank" rel="noopener noreferrer"`.
