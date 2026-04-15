## 2025-04-15 - Gradio Implicit Submission and State Retention
**Learning:** Gradio Textbox components with implicit `.submit()` bindings lack visual cues, leaving users unaware they must press Enter. Additionally, external links in `gr.HTML` navigate away, destroying stateful sessions like WebRTC.
**Action:** Always add `info="Press Enter to submit"` to Textboxes reliant on the Enter key, and use `target="_blank"` with `rel="noopener noreferrer"` and `aria-label` for external links to preserve app state and improve screen reader accessibility.
