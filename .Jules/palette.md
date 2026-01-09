## 2025-02-12 - [Improved Instructions in Gradio Examples]
**Learning:** Gradio examples often lack context. Using `gr.HTML` with inline styling to provide clear instructions (e.g., "Click Record") and setup requirements (e.g., "Ensure API Key is set") significantly improves usability for developers running these examples.
**Action:** Always include a descriptive `gr.HTML` or `gr.Markdown` block at the top of Gradio interfaces to explain the app's purpose and usage instructions.
