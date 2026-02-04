## 2026-02-04 - FastRTC Backend Error
**Learning:** `fastrtc` component can throw `AttributeError: 'NoneType' object has no attribute 'root'` in headless/CI environments during initialization, which persists even with valid configuration.
**Action:** Do not block on this error if functionality (UI rendering) is verified.

## 2026-02-04 - Gradio Theme Deprecation
**Learning:** `gr.Blocks(theme=...)` is deprecated in favor of `.launch(theme=...)`, but the latter doesn't apply the theme globally or to mounted instances correctly in Gradio 5.x.
**Action:** Continue using `gr.Blocks(theme=...)` until Gradio 6.0 or clear migration path for mounted blocks is available.
