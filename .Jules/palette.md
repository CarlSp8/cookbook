## 2025-05-19 - FastRTC UI Accessibility
**Learning:** The 'Get an API Key' link in `fastrtc_ui.py` and `gradio_audio.py` opens in the same tab, which can disrupt the user's flow and potentially lose their chat session. Also missing a clear screen-reader indication that it's an external link.
**Action:** Adding `target="_blank"`, `rel="noopener noreferrer"`, and a descriptive `aria-label` to external links in Gradio HTML components to improve accessibility and retain state.
