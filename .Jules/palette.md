## 2025-06-25 - Secure and Accessible External Links in Gradio
**Learning:** External links embedded in Gradio `gr.HTML` components without `target="_blank"` and `rel="noopener noreferrer"` can cause app state loss and pose security risks. Additionally, using "here" for link text is an accessibility anti-pattern; screen readers need descriptive text (e.g., "Get an API Key") inside the anchor tag along with an `aria-label` indicating it opens in a new tab.
**Action:** Always verify `gr.HTML` external links include proper security attributes and descriptive, accessible link text.

## 2025-06-25 - Explicit Instructions for Implicit Gradio Submissions
**Learning:** When using Gradio's implicit submission mechanisms (like pressing Enter in a `.submit()` mapped `gr.Textbox`), users may not intuitively know how to submit the form without a visible button.
**Action:** Use the `info` parameter on the input component to explicitly instruct the user (e.g., `info="Press Enter to submit"`), provided there is an actual event listener bound to `.submit()`.
