## 2025-05-18 - Gradio State Loss via External Links
**Learning:** Gradio `gr.HTML` components will cause a complete app state loss if external links are clicked without opening in a new tab. Additionally, "here" as link text breaks screen reader flows.
**Action:** Always enforce `target="_blank"` and `rel="noopener noreferrer"` for external links in `gr.HTML`. Use descriptive text and provide an `aria-label` to announce the new tab behavior. Also pass `padding=True` to `gr.HTML` to avoid future deprecation warnings.
