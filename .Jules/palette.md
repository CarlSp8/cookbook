## 2025-02-18 - [Gradio Theme Deprecation Warning Handling]
**Learning:** Gradio 6.x logs a UserWarning when passing `theme` to `gr.Blocks()`, suggesting it should be in `.launch()`. However, moving it to `.launch()` when `gr.load(src=registry)` is used causes a crash or unexpected keyword argument error because `.launch()` on the loaded blocks instance doesn't propagate the theme correctly or conflicts with internal logic.
**Action:** Keep `theme` in `gr.Blocks()` constructor despite the warning for now, until the deprecation becomes a hard error or the `gr.load` pattern supports it properly.

## 2025-02-18 - [WebRTC Component Branding]
**Learning:** The `WebRTC` component (from `gradio-webrtc` or `fastrtc`) supports `icon`, `pulse_color`, and `icon_button_color` which significantly improves branding (e.g. adding Gemini logo). This works even if the underlying library documentation is sparse on these specific arguments.
**Action:** Always add these branding arguments when using `WebRTC` components for Gemini apps to ensure visual consistency.
