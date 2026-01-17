## 2025-05-20 - Dependency Compatibility in Examples
**Learning:** `gradio-webrtc` has strict compatibility requirements with `gradio`. Newer versions (e.g., 5.50.0) can break older libraries due to missing utilities like `wasm_utils`.
**Action:** When working on examples, check `setup` instructions carefully for version constraints. If upgrading dependencies, verify all referenced libraries are compatible.

## 2025-05-20 - Graceful Configuration Handling
**Learning:** In Gradio apps, avoid crashing on missing configuration (like API keys). Instead, render a specific "Setup Required" UI block with instructions.
**Action:** Use `if not config: return error_ui_blocks` pattern in entry points.
