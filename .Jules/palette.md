## 2024-05-24 - Improve API Key Onboarding UX
**Learning:** Gradio Textboxes with implicit submission (`.submit()`) don't naturally indicate how to proceed, and external links in `gr.HTML` can navigate users away from the app state while lacking screen reader context.
**Action:** Always add `info="Press Enter to submit"` to Textboxes bound to `.submit()`, and add `target="_blank"`, `rel="noopener noreferrer"`, and descriptive `aria-label`s to external links in `gr.HTML`.
