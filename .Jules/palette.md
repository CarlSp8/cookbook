
## 2024-05-24 - Implicit Form Submission Clarity
**Learning:** Gradio UI components (like `gr.Textbox`) that rely on implicit submission (e.g. mapping an action to the `.submit()` event when the user presses 'Enter') lack explicit affordances compared to traditional submit buttons. Users might not realize they need to press Enter to proceed, leading to confusion or stalled interactions.
**Action:** When a Gradio app maps a critical action (like revealing protected components or submitting credentials) to a `Textbox.submit()` event without a visible submit button, always use the `info` parameter to explicitly instruct the user (e.g., `info="Press Enter to submit"`). Ensure the `.submit()` event is genuinely mapped, otherwise the instruction is functionally misleading.
