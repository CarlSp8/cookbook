## 2025-03-08 - Gradio Textbox Submit Affordance
**Learning:** Gradio Textboxes with `.submit()` listeners lack visual cues for the Enter key, which can strand users if the textbox is acting as a gate to further UI components.
**Action:** Always add an explicit `info="Press Enter to submit"` to Textboxes mapped to `.submit()`.
