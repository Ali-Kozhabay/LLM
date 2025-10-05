from app.main import app  # or wherever your app instance is
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8011)