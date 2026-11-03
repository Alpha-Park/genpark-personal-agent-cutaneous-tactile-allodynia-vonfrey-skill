---
name: genpark-personal-agent-cutaneous-tactile-allodynia-vonfrey-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for evaluating cutaneous tactile sensitivity, Semmes-Weinstein Von Frey force thresholds, and mechanical allodynia.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Cutaneous Tactile Sensitivity & Mechanical Allodynia (Von Frey) Skill

A sovereign personal agent capability for assessing low-threshold mechanoreceptor tactile acuity, Semmes-Weinstein logarithmic force calibrations, and differentiating peripheral neuropathy from tactile mechanical allodynia.

## Core Capabilities
- **Semmes-Weinstein Logarithmic Scaling**: Converts applied monofilament gram force into standard logarithmic index units.
- **Protective Sensation Threshold**: Evaluates risk of micro-trauma from blunted sensory perception (>2.0 g).
- **Dynamic Mechanical Allodynia Detection**: Identifies abnormal nociceptive cross-talk where gentle touch evokes pain.
- **Ergonomic Tactile Optimization**: Suggests keyboard switch actuation forces, trackpad sensitivities, and sensory re-education drills.

## Fast Invocation
```python
from client import CutaneousTactileVonFreyClient

client = CutaneousTactileVonFreyClient()
res = client.evaluate_tactile_threshold(
    applied_force_grams=0.04,
    detection_reported=True,
    pain_reported=False
)
print("SW Marking:", res["semmes_weinstein_marking"])
print("Tactile Acuity Score:", res["tactile_acuity_score"])
```
