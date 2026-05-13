## 2025-05-13 - External Links and Implicit Submission in Gradio UIs
**Learning:** External links in Gradio `gr.HTML` can cause users to navigate away from the app state, losing their progress (especially WebRTC sessions). Also, Textboxes with `.submit()` handlers lack visual affordance that pressing Enter is required.
**Action:** Always add `target="_blank" rel="noopener noreferrer"` and descriptive `aria-label` to external links in `gr.HTML`. Always add an `info` parameter to `gr.Textbox` components that rely on implicit `.submit()` actions to guide the user.
