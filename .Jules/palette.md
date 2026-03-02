## 2026-03-02 - Gradio UI Interaction Cues
**Learning:** When using Gradio's implicit submission mechanisms (like pressing Enter in a `.submit()` mapped `gr.Textbox`) to hide/reveal components, the lack of an explicit button can leave users unaware of how to proceed.
**Action:** Always add explicit instructional text using the `info` parameter on the triggering input component (e.g., `info="Press Enter to connect"`) to clarify the required interaction pattern.
