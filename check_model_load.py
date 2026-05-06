from pathlib import Path

import tensorflow as tf


def try_load(path: Path):
    try:
        model = tf.keras.models.load_model(str(path), compile=False)
        print(f"{path.name}: OK input={model.input_shape} output={model.output_shape}")
    except Exception as exc:
        print(f"{path.name}: FAIL {str(exc).splitlines()[0]}")


def main():
    base = Path(__file__).resolve().parent
    for filename in ["best_model.keras", "best_model_patched.keras"]:
        path = base / filename
        if path.exists():
            try_load(path)
        else:
            print(f"{filename}: missing")


if __name__ == "__main__":
    main()
