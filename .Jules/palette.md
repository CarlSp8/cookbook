## 2025-04-26 - Gradio Security and Accessibility Patterns
**Learning:** External links in `gr.HTML` components lack native security attributes, risking users navigating away from the web app state unexpectedly, and implicit form submissions (like `gr.Textbox().submit()`) are not discoverable without explicit helper text.
**Action:** Always add `target="_blank"`, `rel="noopener noreferrer"`, and `aria-label` to external links in Gradio HTML components. Always use the `info` parameter to instruct users on implicit submissions (e.g., "Press Enter to submit").
