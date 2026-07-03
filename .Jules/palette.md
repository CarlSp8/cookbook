## 2025-05-15 - Accessible links in Gradio HTML
**Learning:** Using 'here' as link text is an accessibility anti-pattern. External links in Gradio `gr.HTML` can cause app state loss if they don't open in a new tab (`target="_blank"`).
**Action:** Ensure all external links use descriptive text, include `target="_blank" rel="noopener noreferrer"`, and provide an `aria-label` indicating they open in a new tab.
