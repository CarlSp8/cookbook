## 2024-05-15 - Fixed non-descriptive link text and missing target attributes in gr.HTML
**Learning:** Gradio `gr.HTML` components often contain raw HTML links. If they lack `target="_blank"`, navigating away loses the app state. Using "here" as link text is an accessibility anti-pattern.
**Action:** Always wrap descriptive text in the anchor tag, use `target="_blank" rel="noopener noreferrer"`, and add an `aria-label` indicating it opens in a new tab for external links in Gradio HTML.
