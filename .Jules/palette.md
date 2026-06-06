## $(date +%Y-%m-%d) - Accessible Link Text
**Learning:** Using "here" as link text in `gr.HTML` is an accessibility anti-pattern. Screen readers often read links out of context, so the link text itself must be descriptive (e.g., "Get an API Key"). Additionally, external links should use `target="_blank"`, `rel="noopener noreferrer"`, and include an `aria-label` to warn users it opens in a new tab to avoid losing app state.
**Action:** Always wrap the descriptive action inside the anchor tag and include proper target/aria attributes for external links in Gradio UIs.
