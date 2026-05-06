# Tomato Leaf Classifier Interface

Simple Flask interface to load and run predictions using `best_model.keras`.

If model loading fails due to Keras serialization changes, generate and use the patched model file:

```bash
python patch_keras_model.py
```

This creates `best_model_patched.keras`, and the app will load it automatically.

## Project structure

```text
.
|- app/
|  |- __init__.py
|  |- config.py
|  |- model_service.py
|  `- routes.py
|- static/
|  `- styles.css
|- templates/
|  `- index.html
|- best_model.keras
|- best_model_patched.keras (auto-used if present)
|- patch_keras_model.py
|- training.ipynb
|- requirements.txt
`- run.py
```

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python run.py
```

4. Open `http://127.0.0.1:5000` in your browser.

## Notes

- Input size is `224x224`.
- Preprocessing uses `tf.keras.applications.mobilenet_v3.preprocess_input` exactly like training.
- Class names are aligned with the classes printed in `training.ipynb`.
