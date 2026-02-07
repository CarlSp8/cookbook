# Palette's Journal - Critical UX Learnings

## 2026-02-07 - Gradio API Links
**Learning:** External links (like "Get API Key") inside Gradio apps must use `target="_blank" rel="noopener noreferrer"`.
**Action:** Always check `gr.HTML` links for this attribute to prevent users from losing their session state.
