## 2025-04-25 - Implicit Submission Discoverability in Gradio
**Learning:** Gradio `.submit()` events on Textbox components are triggered by pressing Enter, but this interaction is invisible to users. In apps lacking a physical 'Submit' button, this blocks user progression.
**Action:** Always use the `info` parameter on Textbox components mapped to `.submit()` to provide explicit instructions (e.g., `info="Press Enter to submit"`), ensuring there's a bound event listener first.
