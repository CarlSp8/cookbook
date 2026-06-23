## 2024-05-24 - Descriptive External Links in Gradio HTML
**Learning:** External links in Gradio HTML components navigate away and destroy app state unless target="_blank" and rel="noopener noreferrer" are used. Also, using "here" for link text is an accessibility anti-pattern.
**Action:** Wrap descriptive text in the anchor tag, use target="_blank", rel="noopener noreferrer", and add an aria-label indicating it opens in a new tab.
