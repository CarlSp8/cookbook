## 2024-04-12 - Secure External Links in Gradio Apps
**Learning:** Gradio applications lose their active WebSocket and UI state if a user navigates away within the same tab. External links in `gr.HTML` components can cause unintended data loss.
**Action:** Always add `target="_blank"` and `rel="noopener noreferrer"` to external links in Gradio `gr.HTML` components to preserve app state and ensure security.
