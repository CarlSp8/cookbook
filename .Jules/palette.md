## 2025-05-23 - Gradio Polish
**Learning:** Default Gradio themes can feel sterile; `gr.themes.Soft()` immediately makes UIs feel more modern and approachable. Also, links in `gr.HTML` components often replace the current tab, disrupting the app flow; `target="_blank"` is critical for external documentation links.
**Action:** Always apply `gr.themes.Soft()` (or similar) to `gr.Blocks()` and ensure all external links use `target="_blank" rel="noopener noreferrer"`.
