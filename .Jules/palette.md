## 2026-03-18 - [Gradio Textbox Submit Affordance]
**Learning:** Gradio's `gr.Textbox` mapped to a `.submit()` action implicitly uses the 'Enter' key but lacks visual affordances or a submit button by default. This creates a critical UX issue where users do not know how to proceed.
**Action:** Always add an explicit `info='Press Enter to submit'` argument to inputs that rely on implicit `.submit()` triggers to ensure the interface is intuitive.
