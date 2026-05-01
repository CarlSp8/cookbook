## 2024-05-01 - External Links in Gradio HTML Components
**Learning:** External links embedded in Gradio `gr.HTML` components cause users to navigate away from the web app state if clicked directly, which is particularly disruptive for real-time applications like Voice Chat.
**Action:** Always use `target="_blank"` and `rel="noopener noreferrer"` for external links in Gradio `gr.HTML` components. Additionally, include a descriptive `aria-label` (e.g., `aria-label="... (opens in a new tab)"`) to ensure screen reader users are aware of the context switch.
