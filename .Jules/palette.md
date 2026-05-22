## 2025-05-22 - External Links and Implicit Submission in Gradio
**Learning:** Gradio HTML components do not automatically handle external links gracefully, causing users to navigate away from the app state. Additionally, `gr.Textbox.submit()` triggers on 'Enter' but lacks visual affordance by default.
**Action:** Always add `target="_blank"`, `rel="noopener noreferrer"`, and an `aria-label` to external links in `gr.HTML`. Always use the `info` parameter to explicitly instruct users to "Press Enter" when binding to `.submit()`.
