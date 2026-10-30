# -*- coding: utf-8 -*-
import sys, json, math
from client import OpenClawGenParkComputeBroker

client = OpenClawGenParkComputeBroker()

TOOLS = [
    {
        "name": "calculate_preemption_risk",
        "description": "Calculates spot preemption probability and optimal Young checkpointing interval.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "spot_tier": {"type": "string"},
                "duration_hours": {"type": "number"},
                "lambda_arrival": {"type": "number"}
            },
            "required": ["spot_tier", "duration_hours"]
        }
    },
    {
        "name": "run_vcg_spot_auction",
        "description": "Executes multi-unit VCG truthful spot auction for GPU/CPU compute allocation.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "bids": {"type": "array", "items": {"type": "object"}},
                "available_units": {"type": "integer"},
                "reserve_price": {"type": "number"}
            },
            "required": ["bids", "available_units"]
        }
    },
    {
        "name": "optimize_cluster_placement",
        "description": "Calculates Pareto-optimal node cluster placement based on TFLOPS, latency, and cost.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "workload_spec": {"type": "object"},
                "candidate_nodes": {"type": "array", "items": {"type": "object"}}
            },
            "required": ["workload_spec", "candidate_nodes"]
        }
    }
]

def handle_request(req):
    method = req.get("method")
    rid = req.get("id")
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": rid, "result": {"tools": TOOLS}}
    elif method == "tools/call":
        params = req.get("params", {})
        tname = params.get("name")
        args = params.get("arguments", {})
        if tname == "calculate_preemption_risk":
            res = client.calculate_preemption_risk(args["spot_tier"], args["duration_hours"], args.get("lambda_arrival"))
            return {"jsonrpc": "2.0", "id": rid, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        elif tname == "run_vcg_spot_auction":
            res = client.run_vcg_spot_auction(args["bids"], args["available_units"], args.get("reserve_price", 0.50))
            return {"jsonrpc": "2.0", "id": rid, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        elif tname == "optimize_cluster_placement":
            res = client.optimize_cluster_placement(args["workload_spec"], args["candidate_nodes"])
            return {"jsonrpc": "2.0", "id": rid, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        return {"jsonrpc": "2.0", "id": rid, "error": {"code": -32601, "message": "Method not found"}}
    return {"jsonrpc": "2.0", "id": rid, "error": {"code": -32600, "message": "Invalid Request"}}

def main():
    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            resp = handle_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
