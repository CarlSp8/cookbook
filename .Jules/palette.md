## 2025-02-24 - Gradio Textbox Implicit Submission UX
**Learning:** Gradio `gr.Textbox` components mapped to a `.submit()` event lack any inherent visual cue indicating that the user must press "Enter" to proceed, which can lead to user confusion when there is no dedicated "Submit" button.
**Action:** Always add an explicit instruction via the `info` parameter (e.g., `info="Press Enter to submit"`) when utilizing `.submit()` on Textboxes without a supplementary button.
