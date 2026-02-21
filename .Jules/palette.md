## 2026-02-21 - Gradio UX Polish
**Learning:** Gradio interfaces reset when users navigate away, causing frustration if links don't open in new tabs. Also, adding `info` tooltips and consistent `theme` improves usability significantly.
**Action:**
1. Always add `target="_blank" rel="noopener noreferrer"` to external links in `gr.HTML` components.
2. Use `info` parameter for complex inputs.
3. Apply `gr.themes.Soft()` for a cleaner look.
