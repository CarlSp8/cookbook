## 2025-02-12 - Gradio Theme Compatibility
**Learning:** Gradio 6.0 moves `theme` from `gr.Blocks()` to `.launch()`, but 5.x (used here) requires it in `gr.Blocks()`. Passing it to `launch()` in 5.x causes errors.
**Action:** When working with Gradio < 6.0, instantiate themes in `gr.Blocks(theme=...)` despite 6.0 warnings to ensure backward compatibility.
