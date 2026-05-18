## 2025-05-18 - Improve Gradio Implicit Submission and External Links
**Learning:** Gradio Textboxes with `.submit()` actions lack visual cues for implicit submission (like pressing Enter), and external links in `gr.HTML` can cause users to navigate away from the app state if not properly configured with `target="_blank"` and accessibility attributes.
**Action:** Always add `info="Press Enter to submit"` to Textboxes mapped to a `.submit()` event, and ensure external links in HTML components use `target="_blank"`, `rel="noopener noreferrer"`, and descriptive `aria-label`s.
