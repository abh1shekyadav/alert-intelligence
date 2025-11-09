from typing import Dict


def enrich_alert(alert: Dict) -> Dict:
    severity_weight_map ={
        "critical" :  5,
        "high" : 4,
        "medium" : 3,
        "low" : 2,
        "info" : 1
    }

    message = alert.get("message", "").lower()
    category = None
    if "cpu" in message:
        category = "CPU"
    elif "memory" in message:
        category = "Memory"
    elif "disk" in message:
        category = "Disk"
    else:
        category = "General"

    return {
        "service_owner": "infra-team",
        "category": category,
        "severity_weight": severity_weight_map.get(alert.get("severity", "info"), 1),
        "tags": [category.lower(), alert.get("severity", "").lower()]
    }