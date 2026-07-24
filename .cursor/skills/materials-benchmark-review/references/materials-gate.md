# Materials qualification gate

Classify as `MAT_CORE`, `MAT_METHOD`, `MAT_WRAPPER`, `NON_MAT`, or `AMBIGUOUS`.
Use the instruction's problem background, approach, reproduction target, and
actual checker-enforced work—not keywords or directory names.

Evidence must cover materials object/system, data, scientific operation,
endpoint, and domain dependence. `NON_MAT` triggers `NON_MATERIALS_TASK` and
`REJECT`. A wrapper passes only if the scored work still requires substantive
materials reasoning; otherwise reject or mark ambiguous pending evidence.

Extract the claimed capability and verify:

```text
claimed capability → necessary operation → observable core output
→ checker-enforced evidence
```
