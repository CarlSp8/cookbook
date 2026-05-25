## 2025-05-25 - External Links in Gradio Apps
**Learning:** Gradio web applications can easily lose state if a user navigates away within the same tab. Therefore, all external links embedded in `gr.HTML` components must open in a new tab using `target="_blank"`.
**Action:** Always include `target="_blank"`, `rel="noopener noreferrer"`, and a descriptive `aria-label` (e.g., `aria-label="... (opens in a new tab)"`) for external links in Gradio applications to prevent state loss and ensure screen reader accessibility.
