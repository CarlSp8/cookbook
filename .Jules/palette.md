## 2025-04-21 - Gradio Implicit Form Submission Discovery
**Learning:** Gradio Textbox components with `.submit()` handlers do not provide implicit visual cues or instructions to the user that pressing 'Enter' will trigger an action. This leaves users guessing how to proceed when there is no explicit "Submit" button.
**Action:** Always add an explicit instruction via the `info` parameter (e.g., `info="Press Enter to submit"`) to Gradio text inputs that map to `.submit()` to ensure intuitive interaction.

## 2025-04-21 - Gradio External Links Accessibility
**Learning:** Using basic HTML for external links in `gr.HTML` can lead users to unintentionally navigate away from the Single Page Application state of Gradio apps.
**Action:** Always use explicit HTML anchors with `target="_blank"`, `rel="noopener noreferrer"`, and descriptive `aria-label`s for external resources.
