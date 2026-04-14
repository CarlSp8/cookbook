## 2025-02-23 - Gradio External Links and Implicit Submits
**Learning:** External links embedded in Gradio HTML components can navigate users away from the app state. Implicit form submissions (like Enter in a Textbox) aren't obvious without explicit UI instruction.
**Action:** Always add `target="_blank"`, `rel="noopener noreferrer"`, and `aria-label` for screen readers to external links in `gr.HTML`. Always add the `info` parameter to `gr.Textbox` if it uses `.submit()` for implicit submission. Use preferred Gemini brand colors `rgb(59, 130, 246)`.
