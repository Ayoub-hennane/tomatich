from functools import lru_cache
from io import BytesIO

import numpy as np

try:
    # Try TensorFlow 2.x first
    import tensorflow as tf
    from tensorflow.keras.applications.mobilenet_v3 import preprocess_input
    BACKEND = "tensorflow"
except (ImportError, AttributeError):
    # Fallback to Keras 2
    import keras as tf
    from keras.applications.mobilenet_v3 import preprocess_input
    BACKEND = "keras"

from PIL import Image

from .config import CLASS_NAMES, IMG_SIZE, MODEL_PATH


@lru_cache(maxsize=1)
def load_model():
    """Load model with compatibility for both Keras 2 and 3."""
    try:
        if BACKEND == "tensorflow":
            return tf.keras.models.load_model(str(MODEL_PATH), compile=False)
        else:
            return tf.models.load_model(str(MODEL_PATH), compile=False)
    except Exception as e:
        print(f"Load error: {str(e)[:200]}")
        raise RuntimeError(f"Could not load model: {str(e)[:100]}") from e


def preprocess_image(file_bytes: bytes) -> np.ndarray:
    image = Image.open(BytesIO(file_bytes)).convert("RGB")
    image = image.resize(IMG_SIZE)
    array = np.asarray(image, dtype=np.float32)
    array = np.expand_dims(array, axis=0)
    return preprocess_input(array)


def predict_image(file_bytes: bytes) -> dict:
    model = load_model()
    x = preprocess_image(file_bytes)
    probs = model.predict(x, verbose=0)[0]

    best_idx = int(np.argmax(probs))
    confidence = float(probs[best_idx])

    top_indices = np.argsort(probs)[::-1][:3]
    top_predictions = [
        {
            "label": CLASS_NAMES[int(i)],
            "confidence": float(probs[int(i)]),
        }
        for i in top_indices
    ]

    return {
        "label": CLASS_NAMES[best_idx],
        "confidence": confidence,
        "top_predictions": top_predictions,
    }
