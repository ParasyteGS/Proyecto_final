from src import create_app
import os
from dotenv import load_dotenv

load_dotenv()


app = create_app()
app.secret_key = os.getenv("SECRET_KEY")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
