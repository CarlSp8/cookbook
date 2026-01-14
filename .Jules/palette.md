## 2025-05-15 - Simplifying Single-View Gradio Demos
**Learning:** Single-view Gradio demos often wrap content in redundant `Tabs`, adding unnecessary visual noise.
**Action:** For single-page tools, remove `Tabs`, use `gr.themes.Soft()` for instant polish, and use centered `gr.HTML` headers with specific usage notes (e.g. "Interruptions not supported") to manage user expectations.
