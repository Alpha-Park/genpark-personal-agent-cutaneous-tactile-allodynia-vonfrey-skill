# Cutaneous Tactile Sensitivity & Mechanical Allodynia (Von Frey) Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of cutaneous mechanoreceptive tactile thresholds via Von Frey Semmes-Weinstein monofilaments and mechanical allodynia detection.

```mermaid
flowchart TD
    Monofilament["Von Frey Filament Bending Force (Grams / mg)"] --> SW_Formula["Semmes-Weinstein Logarithmic Scaling (log10(10*mg))"]
    SW_Formula --> ThresholdStrat["Psychophysical Sensory Stratification"]
    ThresholdStrat --> AcuityEngine["Tactile Acuity & Allodynia Scoring"]
    AcuityEngine --> Agent["OpenClaw / Hermes Personal Agent Actions"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Clinical Neuro-Psychophysical Standards**: Implements validated logarithmic force equations.
- **Sensory Blunting vs Allodynia Differentiation**: Accurately classifies peripheral neuropathy vs central pain sensitization.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import CutaneousTactileVonFreyClient

client = CutaneousTactileVonFreyClient()
result = client.evaluate_tactile_threshold(
    applied_force_grams=0.04,
    detection_reported=True
)
print("SW Marking:", result["semmes_weinstein_marking"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
