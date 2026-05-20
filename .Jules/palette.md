## 2024-05-24 - Gradio SPA Navigation and Implicit Submissions
**Learning:** External links embedded in Gradio `gr.HTML` components can cause users to accidentally navigate away from the SPA, losing state. Additionally, `gr.Textbox` components tied to `.submit()` lack visual cues that they require an 'Enter' keypress.
**Action:** Always use `target="_blank"`, `rel="noopener noreferrer"`, and an explicit `aria-label` for external links. Always add an `info` parameter to explicitly instruct users for implicit submission textboxes.
