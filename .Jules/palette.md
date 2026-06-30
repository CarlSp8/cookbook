## 2025-02-21 - Link Accessibility and Implicit Submission
**Learning:** External links in Gradio `gr.HTML` can cause app state loss if not opened in a new tab. Using 'here' as link text is an accessibility anti-pattern. Also, implicit submission via `gr.Textbox().submit()` requires explicit user instruction since the action isn't visually obvious.
**Action:** Always use `target="_blank"` with `rel="noopener noreferrer"` for external links, and use descriptive link text with an `aria-label`. Always provide an `info` parameter on Textbox components mapped to `.submit()` events.
