## 2024-05-24 - Gradio Link State Loss & Accessibility
**Learning:** External links inside Gradio `gr.HTML` components without `target="_blank"` cause full page navigation, resulting in complete loss of application state. Additionally, using "here" as link text breaks screen reader accessibility.
**Action:** Always use descriptive link text (never "here"), include `target="_blank"` and `rel="noopener noreferrer"`, and provide an `aria-label` indicating it opens in a new tab to preserve app state and ensure accessibility.
