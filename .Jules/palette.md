## 2025-06-21 - Accessible external links in Gradio HTML components
**Learning:** Using vague link text like "here" without `target="_blank"`, `rel="noopener noreferrer"`, and an `aria-label` causes security risks, app state loss, and screen reader confusion in Gradio apps.
**Action:** Always wrap descriptive text in anchor tags, add `target="_blank"`, `rel="noopener noreferrer"`, and an `aria-label` explaining that the link opens in a new tab.
