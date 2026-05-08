## 2023-10-25 - Improve External Links and Implicit Submission in Gradio UIs
**Learning:** External links in `gr.HTML` can accidentally navigate users away from the web app state, and implicit submissions (like pressing Enter in a `gr.Textbox` mapped to `.submit()`) lack visual cues.
**Action:** Always add `target="_blank"`, `rel="noopener noreferrer"`, and a descriptive `aria-label` to external links. Use the `info` parameter in Gradio components with implicit submission to explicitly instruct the user to press Enter.
