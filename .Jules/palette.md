## 2026-02-13 - Migrating from gradio-webrtc to fastrtc for UX
**Learning:** Legacy `gradio-webrtc` components limit UX flexibility (e.g., hard to pass UI inputs like API keys to handlers). `fastrtc` offers a `start_up` method with `wait_for_args` that elegantly solves this, allowing rich UI inputs (keys, voices) to drive backend streaming logic.
**Action:** Prefer `fastrtc` for all new WebRTC-based Gradio examples to enable better configuration UX.
