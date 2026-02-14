import uvicorn
from lesson22.api_develepment.api import app


if__name__ == "__main__":
uvicorn.run(app, host="127.0.0.1", port=8000)