## 2025-02-24 - Gradio Link Navigation State Loss
**Learning:** External links embedded in Gradio `gr.HTML` components can cause users to lose their web app state (like loaded models or active WebRTC sessions) if they open in the same tab. Additionally, implicit form submissions via `.submit()` lack affordance without explicit helper text.
**Action:** Always add `target="_blank"`, `rel="noopener noreferrer"`, and `aria-label="... (opens in a new tab)"` to external links in `gr.HTML`. Use the `info` prop on `gr.Textbox` to instruct users to press Enter when bound to a `.submit()` event.
