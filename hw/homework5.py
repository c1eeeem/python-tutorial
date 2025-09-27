def is_safe_bridge(bridge: str):
    bridge = bridge.strip()
    return " " not in bridge

print(is_safe_bridge("####"))     # True
print(is_safe_bridge("## ####"))  # False
print(is_safe_bridge("#"))        # True

