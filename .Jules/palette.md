## 2024-05-04 - Improve Gradio Info Text Discoverability
**Learning:** In Gradio interfaces requiring implicit form submission (like hitting "Enter" in a text box), the visual prompt or instruction is not implicitly clear.
**Action:** Enhance user clarity by explicitly using the `info` attribute in `gr.Textbox` to provide immediate, actionable instructions ("Press Enter to submit") without cluttering the UI, as seen in the API key text box.
