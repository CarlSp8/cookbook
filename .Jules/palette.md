## 2025-02-13 - Graceful Configuration Failure
**Learning:** Users often run examples without reading prerequisites (like API keys). Crashing with a traceback is a poor experience.
**Action:** Always wrap the main app logic in a configuration check. If missing, render a `gr.Markdown` warning with instructions instead of the functional app.
