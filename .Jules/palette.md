## 2025-10-24 - Gradio Implicit Submission and Link Navigation Constraints
**Learning:** Gradio UI state can be lost if embedded HTML links navigate away from the app. Additionally, Gradio Textbox components with bound `.submit()` listeners lack visual affordances indicating that pressing "Enter" will trigger an action.
**Action:** Always add `target="_blank"`, `rel="noopener noreferrer"`, and an `aria-label` to external links in `gr.HTML`. Always add an `info="Press Enter to submit"` property to `gr.Textbox` elements that rely on implicit `.submit()` triggers.
