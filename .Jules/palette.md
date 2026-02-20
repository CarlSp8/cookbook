## 2025-02-13 - [Migrating Gradio Audio to FastRTC]
**Learning:** `gradio-webrtc` is deprecated and broken in the current environment; the repository is migrating to `fastrtc`. `fastrtc` offers a drop-in replacement `StreamHandler` and `WebRTC` components that support better UX customization (icons, pulse color).
**Action:** When working with WebRTC in Gradio within this repo, always use `fastrtc`. Use `gr.themes.Soft()` for quick visual wins.
