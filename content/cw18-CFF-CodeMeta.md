---
title: "Aligning the Citation File Format and CodeMeta"
author:
- Stephan Druskat
year: 2018
type: hack-ideas
tags:
- citation
- CFF
---

Collaborations Workshop 2018 - 2018-03-26

Aligning the Citation File Format and CodeMeta -

HP3-CW18

**Hackday Idea Proposer**

Stephan Druskat - stephan.druskat@hu-berlin.de

---


**Context / Research Domain**

*The domain is: Software Citation Implementations*

**Problem**

*The Citation File Format (CFF, [https://citation-file-format.github.io](https://citation-file-format.github.io/)) is a human-writable and -readable, machine-readable format for the provision of software citation metadata.*

*As such, it should be aligned with the evolving standard for providing \*general\* software metadata, CodeMeta ([https://codemeta.github.io](https://codemeta.github.io/)). This is because:*

1. Resources in the small software citation implementation community sholdn't be stretched across more projects than absolutely necessary.
2. CodeMeta is enjoying upstream uptake by, e.g., repositories and is likely to gain more* support, a second format would not and \*should\* not aim to replicate those efforts.
3. It seems as if CFF could be a valid and accessible way for \*end users\* to provide such* metadata and has enjoyed some uptake, but should also be usable as a source format for CodeMeta in a way that ensures no information is lost.

**Solution**

- This activity should ideally streamline CFF and CodeMeta keys to lower the barrier for  completely automatic YAML-JSON conversion to and fro.
- It should be investigated whether CFF can be converted to CodeMeta without losing information (e.g., linked data)
- *Can CFF YAML represent linked data without adding format overhead (such as enforcing key namespaces or similar)*
- *Can CFF be used for:*
   - *linkage (req)*
   - *credit (req)*
   - *discovery (req)*
   - *reproducibility*
   - *provenance*
- *This activity can also be used to figure out if “tooling” is the omnipotent answer for issues in this space, and whether tooling can be developed to enforce best practices (e.g., from the Software Citation Principles)*


