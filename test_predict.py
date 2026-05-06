from pathlib import Path

from app.model_service import predict_image


def main():
    image_path = Path("images.jpeg")
    result = predict_image(image_path.read_bytes())
    print(result)


if __name__ == "__main__":
    main()
