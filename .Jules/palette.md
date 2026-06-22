## 2025-05-23 - Gradio App State Preservation on External Links
**Learning:** External links inside gr.HTML can overwrite the current app tab, causing the user to lose their Gradio app state entirely, which is very disruptive for realtime apps (like WebRTC). Additionally, screen readers struggle with "here" link texts.
**Action:** Always use target="_blank" and rel="noopener noreferrer" for external links in gr.HTML, and wrap descriptive text inside the anchor rather than using "here". Add aria-label to indicate it opens in a new tab.
