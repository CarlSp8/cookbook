## 2025-05-18 - Gradio Link Navigation
**Learning:** External links embedded in `gr.HTML` components replace the application instance by default, causing users to lose their session and state.
**Action:** Always enforce `target="_blank"` and `rel="noopener noreferrer"` for any external anchors within Gradio interfaces to ensure the app remains open.
