## 2025-05-23 - Gradio WebRTC Deprecation
**Learning:** The `gradio-webrtc` package is deprecated and fails to import due to missing `gradio.wasm_utils`. `fastrtc` is a functional drop-in replacement that works with current dependencies.
**Action:** When working on Gradio apps using WebRTC, replace `gradio-webrtc` imports with `fastrtc`.

## 2025-05-23 - Gradio Theme Deprecation Warning
**Learning:** `gr.Blocks(theme=...)` issues a deprecation warning, but passing `theme` to `gr.load(...).launch()` when `src` is a function (like `registry`) is complicated because `gr.load` might wrap the blocks. Sticking to `gr.Blocks(theme=...)` inside the registry function ensures the theme is applied correctly for now.
**Action:** Ignore the deprecation warning until Gradio 6.0 or until `gr.load` mechanics are clearer.
