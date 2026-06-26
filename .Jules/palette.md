## 2025-05-16 - Gradio HTML Link Accessibility Constraints
**Learning:** External links embedded in Gradio `gr.HTML` components must use `target="_blank"` and `rel="noopener noreferrer"` to prevent app state loss, and "here" link text is an accessibility anti-pattern.
**Action:** Always wrap descriptive text in the anchor tag and use standard secure link attributes with `aria-label` indicating it opens in a new tab.

## 2025-05-16 - Gradio Implicit Submission Discoverability
**Learning:** Gradio's `.submit()` binding on Textboxes operates implicitly (e.g. via Enter key) without visual cues, causing discoverability issues.
**Action:** Add explicit `info="Press Enter to submit"` parameters to Textbox components that rely on `.submit()` for state transitions.
