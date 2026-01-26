## 2025-02-24 - Gradio WebRTC Migration
**Learning:** `gradio-webrtc` is deprecated and broken with recent Gradio versions. `fastrtc` is the replacement and offers a drop-in replacement for `StreamHandler` and `WebRTC` components.
**Action:** When working on Gradio audio apps, always check for `gradio-webrtc` and migrate to `fastrtc` proactively.
