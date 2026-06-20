## 2025-06-20 - Gradio HTML Link State Loss
**Learning:** External links embedded within Gradio `gr.HTML` components must open in a new tab (`target="_blank"`), otherwise users navigating away will lose their current application state (like loaded models or active WebRTC connections).
**Action:** Always append `target="_blank"` and `rel="noopener noreferrer"` to external links in `gr.HTML` components, and include an `aria-label` to inform screen reader users that the link opens a new tab.
