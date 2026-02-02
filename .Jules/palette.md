## 2025-05-15 - Modernizing Real-time Audio UI
**Learning:** Migrating from `gradio-webrtc` to `fastrtc` enables richer UI customization (icons, pulse colors) for WebRTC components, essential for branded experiences.
**Action:** When working with Gradio WebRTC apps, prefer `fastrtc` and leverage `icon` and `pulse_color` props to align with brand identity (e.g., Gemini blue).

## 2025-05-15 - Gradio Theme Deprecation
**Learning:** `gr.Blocks(theme=...)` triggers a deprecation warning in Gradio 5.x favoring `.launch(theme=...)`, but moving it to `.launch()` on a `Blocks` instance currently causes an error.
**Action:** Stick to `gr.Blocks(theme=...)` constructor for now and monitor Gradio updates for a fix or clearer migration path.
