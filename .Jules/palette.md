## 2023-10-24 - Gradio Accessibility and Interaction Clarity
**Learning:** Gradio `gr.HTML` links lack default target/rel attributes which causes app state loss, and text inputs with `.submit()` lack visual cues that "Enter" is actionable. Using "here" for link text is an accessibility anti-pattern.
**Action:** Always add `target="_blank"` and `rel="noopener noreferrer"` to external links with descriptive text and an `aria-label`. Use the `info` parameter (e.g., `info="Press Enter to submit"`) on inputs with mapped submission handlers.
