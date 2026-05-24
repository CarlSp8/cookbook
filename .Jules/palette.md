## 2025-02-14 - Improve API Key entry UX and link accessibility
**Learning:** External links in Gradio HTML block components can cause users to navigate away from the app state if they don't open in a new tab. Additionally, Gradio's implicit `.submit()` on Textboxes isn't always obvious to users.
**Action:** Always add `target="_blank"` and `rel="noopener noreferrer"` with an `aria-label` for screen readers to external links. Provide `info` text on Textboxes that trigger a `.submit()` action to clarify that pressing "Enter" is required.
