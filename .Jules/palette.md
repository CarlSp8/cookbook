## 2023-10-25 - External Link Accessibility in Gradio
**Learning:** External links embedded in Gradio `gr.HTML` components must use `target="_blank"` and `rel="noopener noreferrer"` to prevent users from accidentally navigating away from the web app state (losing their session), and must include a descriptive `aria-label` (e.g., `aria-label="... (opens in a new tab)"`) for better screen reader accessibility.
**Action:** Always add `target="_blank"`, `rel="noopener noreferrer"`, and a descriptive `aria-label` when adding external links within Gradio HTML components.
