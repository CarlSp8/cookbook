## 2025-02-23 - Gradio Header Polish
**Learning:** Standard `gr.Markdown("# Title")` feels cold. `gr.HTML` with centered alignment, emojis, and subtitles creates a much friendlier "app-like" first impression.
**Action:** Always wrap main titles in a centered `div` with a subtitle when building Gradio demos.

## 2025-02-23 - Brand Identity in WebRTC
**Learning:** `fastrtc.WebRTC` components can be heavily branded with icons and pulse colors. This transforms a generic tech demo into a branded product experience.
**Action:** Always check if `icon` and `pulse_color` can be set to match the brand identity (e.g. Gemini blue `rgb(59, 130, 246)`).
