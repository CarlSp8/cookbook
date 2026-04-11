## 2025-02-27 - Gradio Implicit Submit & External Links
**Learning:** Gradio implicit submissions (like `Textbox.submit`) lack visual affordances, and external links in `gr.HTML` lack default target attributes, which can disrupt the single-page application state if a user navigates away.
**Action:** Always add `info="Press Enter..."` to inputs with bound `.submit()` events, and explicitly add `target="_blank" rel="noopener noreferrer"` to any external links within `gr.HTML` blocks to preserve application context and security.
