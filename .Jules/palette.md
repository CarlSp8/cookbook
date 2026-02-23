## 2025-02-19 - Playwright Verification of WebRTC Components
**Learning:** Locating Gradio WebRTC components by text ("Audio") in Playwright can be ambiguous if the label text appears in descriptions or other elements.
**Action:** Use `exact=True` or `get_by_role` with specific names to target component labels reliably during verification.

## 2025-02-19 - Gradio Theme Deprecation
**Learning:** Gradio 5.x warns about `theme` in `Blocks()` constructor, but moving it to `launch()` causes errors in some contexts.
**Action:** Keep `theme` in `Blocks()` constructor for now despite warnings until the library fully supports the migration path.
