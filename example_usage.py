# -*- coding: utf-8 -*-
from client import OpenClawGenParkComputeBroker

broker = OpenClawGenParkComputeBroker()

# 1. Preemption Risk
risk = broker.calculate_preemption_risk("tier_spot_standard", 8.0, 0.04)
print("Preemption Risk Analysis:")
print(f"  P(interruption) = {risk['preemption_probability']*100:.1f}%, Checkpoint Interval = {risk['optimal_checkpoint_interval_hours']}h")

# 2. VCG Auction
bids = [
    {"bidder_id": "agent_deepseek", "bid_price": 2.80, "units_requested": 4},
    {"bidder_id": "agent_claude", "bid_price": 2.50, "units_requested": 2},
    {"bidder_id": "agent_llama", "bid_price": 1.90, "units_requested": 3},
    {"bidder_id": "agent_crawler", "bid_price": 0.80, "units_requested": 5}
]
auction = broker.run_vcg_spot_auction(bids, available_units=6, reserve_price=1.0)
print("\nVCG Auction Clearance:")
print(f"  Clearing Price: ${auction['clearing_unit_price']}/unit, Allocated: {auction['allocated_units_total']}/6")

# 3. Cluster Optimization
candidates = [
    {"node_id": "gpu_node_1", "accelerator_type": "H100_SXM5", "tflops": 989.0, "price_per_hour": 3.80, "interconnect_gbs": 900.0, "latency_ms": 12.0, "preemption_lambda": 0.02},
    {"node_id": "gpu_node_2", "accelerator_type": "A100_80GB", "tflops": 312.0, "price_per_hour": 1.60, "interconnect_gbs": 600.0, "latency_ms": 18.0, "preemption_lambda": 0.04},
    {"node_id": "gpu_node_3", "accelerator_type": "RTX_4090", "tflops": 165.0, "price_per_hour": 0.50, "interconnect_gbs": 64.0, "latency_ms": 35.0, "preemption_lambda": 0.08}
]
opt = broker.optimize_cluster_placement({"min_tflops": 100.0, "max_price_per_hour": 5.0}, candidates)
print("\nOptimal Cluster Node:")
print(f"  Selected: {opt['top_placement_recommendation']['node_id']} (Score: {opt['top_placement_recommendation']['pareto_efficiency_score']})")
