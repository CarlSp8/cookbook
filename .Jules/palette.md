## 2025-02-28 - External Links in Gradio HTML
**Learning:** When adding links in Gradio `gr.HTML` components, clicking them can navigate away from the app, causing state loss. Using "here" as link text is also an accessibility anti-pattern.
**Action:** Always use descriptive link text wrapped in the anchor tag with an `aria-label` indicating it opens in a new tab, and add `target="_blank"` and `rel="noopener noreferrer"`.
