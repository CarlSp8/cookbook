## 2025-06-19 - Gradio Implicit Submit and App State Loss
**Learning:** Gradio's `gr.Textbox` implicit `.submit()` event lacks visual affordance, leaving users confused. Furthermore, embedding standard links in `gr.HTML` without `target="_blank"` causes complete app state loss because Gradio functions as a single-page application.
**Action:** Always provide explicit instructional `info` text on implicit-submit inputs, and rigorously secure external links with `target="_blank"` and `rel="noopener noreferrer"` to protect Gradio app state.
