def is_safe_bridge(bridge: str):
    return " " not in bridge

print(is_safe_bridge("####"))     # True
print(is_safe_bridge("## ####"))  # False
print(is_safe_bridge("#"))        # True

