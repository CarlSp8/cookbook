## 2025-10-27 - Gradio Theme Deprecation Confusion
**Learning:** The deprecation warning in Gradio 5.50.0 suggests moving `theme` to `launch()`, but doing so causes a `TypeError`. The `theme` parameter is still required in the `gr.Blocks()` constructor for now.
**Action:** Ignore the deprecation warning about `theme` location until a newer version of Gradio actually supports it in `launch()`.

## 2025-10-27 - Gradio Micro-UX
**Learning:** Adding `info` parameters to Gradio inputs (`Textbox`, `Dropdown`) is a high-value, low-effort accessibility win that provides context without cluttering the UI.
**Action:** Systematically check all Gradio inputs for missing `info` tooltips.
