## 2025-05-18 - Graceful Error Handling in Gradio
**Learning:** Hard crashes due to missing environment variables (like API keys) are a major UX barrier, especially in demo apps.
**Action:** Always wrap the main UI entry point (e.g., `registry` or `main`) with a check for required config. If missing, return a `gr.Blocks` instance containing a clear, visually distinct warning message (e.g., using `gr.Markdown` with styled HTML) instead of letting the app crash or showing a traceback.
