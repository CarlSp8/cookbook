## 2025-05-19 - FastRTC replaces Gradio-WebRTC
**Learning:** `gradio-webrtc` is deprecated and broken with newer Gradio versions. `fastrtc` is the replacement library that offers compatible `StreamHandler` and `WebRTC` components with additional features (like icon customization).
**Action:** When working with WebRTC components in this repo, always use `fastrtc` and migrate any legacy `gradio-webrtc` usage.
