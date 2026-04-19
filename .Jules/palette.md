## 2025-04-19 - Gradio Implicit Submission Feedback
**Learning:** Gradio Textbox components with `.submit()` event handlers lack visual indicators that pressing 'Enter' will submit the form, leading to a confusing user experience where they might wait indefinitely or look for a non-existent button.
**Action:** Always add an explicit `info="Press Enter to submit"` parameter to `gr.Textbox` components that rely on implicit keyboard submission, but only after verifying a `.submit()` handler is actively bound.

## 2025-04-19 - Gradio HTML Component Link Accessibility
**Learning:** External links embedded within `gr.HTML` components in Gradio apps can cause users to accidentally navigate away from the current stateful web app if they are not explicitly configured to open in a new tab. This also poses a security risk and an accessibility gap for screen readers.
**Action:** Always append `target="_blank"`, `rel="noopener noreferrer"`, and a descriptive `aria-label` (e.g., `aria-label="... (opens in a new tab)"`) to any `<a>` tags rendered inside `gr.HTML` blocks.
