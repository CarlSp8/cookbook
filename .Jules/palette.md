## 2025-05-26 - Gradio Audio Chat UX
**Learning:** Gradio's default theme is stark; applying `gr.themes.Soft()` is a low-effort, high-impact visual upgrade.
**Action:** Always consider `gr.themes.Soft()` for new Gradio demos unless a specific custom theme is required.

## 2025-05-26 - Gradio Empty States
**Learning:** Gradio apps often launch with empty inputs and no guidance. A simple centered HTML block with instructions significantly improves the "first paint" experience.
**Action:** Always add a `gr.HTML` or `gr.Markdown` block with explicit "Get Started" instructions above the main interactive component.
