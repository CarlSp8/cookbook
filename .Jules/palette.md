## 2024-05-24 - Gradio Implicit Submit Feedback
**Learning:** Gradio Textboxes bound to `.submit()` handlers do not provide native visual cues indicating that users must press 'Enter'. This causes friction when no explicit submit button exists.
**Action:** Always add an explicit `info="Press Enter to submit"` parameter to these textboxes to clarify the interaction model.
