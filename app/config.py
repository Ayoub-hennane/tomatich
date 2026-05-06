from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PATCHED_MODEL_PATH = BASE_DIR / "best_model_patched.keras"
MODEL_PATH = PATCHED_MODEL_PATH if PATCHED_MODEL_PATH.exists() else BASE_DIR / "best_model.keras"

IMG_SIZE = (224, 224)
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}

CLASS_NAMES = [
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_Spider_mites_Two_spotted_spider_mite",
    "Tomato__Target_Spot",
    "Tomato__Tomato_YellowLeaf__Curl_Virus",
    "Tomato__Tomato_mosaic_virus",
    "Tomato_healthy",
]
