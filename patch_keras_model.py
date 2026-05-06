import json
import zipfile
from pathlib import Path


def remove_quantization_config(obj):
    removed = 0
    if isinstance(obj, dict):
        if "quantization_config" in obj:
            obj.pop("quantization_config", None)
            removed += 1
        for key, value in list(obj.items()):
            child_removed = remove_quantization_config(value)
            removed += child_removed
    elif isinstance(obj, list):
        for item in obj:
            child_removed = remove_quantization_config(item)
            removed += child_removed
    return removed


def main():
    src = Path("best_model.keras")
    dst = Path("best_model_patched.keras")

    with zipfile.ZipFile(src, "r") as zin:
        metadata = zin.read("metadata.json")
        config = json.loads(zin.read("config.json"))
        weights = zin.read("model.weights.h5")

    removed_count = remove_quantization_config(config)

    with zipfile.ZipFile(dst, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        zout.writestr("metadata.json", metadata)
        zout.writestr("config.json", json.dumps(config))
        zout.writestr("model.weights.h5", weights)

    print(f"patched: {dst}")
    print(f"removed quantization_config keys: {removed_count}")


if __name__ == "__main__":
    main()
