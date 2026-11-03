"""
MCP Server for Cutaneous Tactile Sensitivity & Mechanical Allodynia (Von Frey) Skill.
Exposes JSON-RPC Model Context Protocol tools for evaluating mechanoreceptive force thresholds and tactile acuity.
"""

import sys
import json
from typing import Dict, Any
from client import CutaneousTactileVonFreyClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_tactile_threshold",
                "description": "Calculates Von Frey Semmes-Weinstein marking, tactile mechanoreceptive acuity score, and allodynia/neuropathy classification.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "applied_force_grams": {
                            "type": "number",
                            "description": "Bending force of monofilament in grams (e.g. 0.04 g for light touch, 2.0 g for protective threshold)."
                        },
                        "detection_reported": {
                            "type": "boolean",
                            "description": "Whether tactile stimulus was successfully detected by the subject.",
                            "default": True
                        },
                        "pain_reported": {
                            "type": "boolean",
                            "description": "Whether the tactile stimulus elicited a painful sensation (allodynia).",
                            "default": False
                        },
                        "test_site": {
                            "type": "string",
                            "description": "Anatomical testing site (e.g. FINGERTIP, PALM, DORSUM_FOOT).",
                            "default": "FINGERTIP"
                        }
                    },
                    "required": ["applied_force_grams"]
                }
            }
        ]
    }


def handle_request(client: CutaneousTactileVonFreyClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_tactile_threshold":
            res = client.evaluate_tactile_threshold(
                applied_force_grams=float(args.get("applied_force_grams", 0.04)),
                detection_reported=bool(args.get("detection_reported", True)),
                pain_reported=bool(args.get("pain_reported", False)),
                test_site=str(args.get("test_site", "FINGERTIP"))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method {name} not found"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": "Invalid request"
            }
        }


def main():
    client = CutaneousTactileVonFreyClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": str(e)}
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
