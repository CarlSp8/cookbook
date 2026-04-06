## 2026-04-06 - Gradio Textbox Submit Discoverability
**Learning:** Gradio Textbox implicitly binds the 'Enter' key to `.submit()` handlers, but offers no visual affordance by default. Also, Gradio HTML components do not automatically add `target='_blank'` to external links, causing accidental SPA navigation.
**Action:** Always add `info='Press Enter to submit'` to Textboxes with `.submit()` events, and explicitly add `target='_blank' rel='noopener noreferrer'` to links in `gr.HTML`.
