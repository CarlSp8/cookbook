## 2026-04-07 - External Links in Gradio HTML Components
**Learning:** When adding external links using `gr.HTML` in a Gradio application, omitting `target="_blank"` can cause the user to accidentally navigate away from the app, losing their current state (such as chat history or uploaded files). Additionally, `rel="noopener noreferrer"` should be included for security.
**Action:** Always verify that `<a>` tags in `gr.HTML` include `target="_blank" rel="noopener noreferrer"`.
