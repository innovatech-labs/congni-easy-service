# CogniEasy Service

- This project holds the back-end service of the CogniEasy app

## Getting started
1. Clone this git repository to your local computer
2. In the project repo, create a virtual environment by running `python3 -m venv ./venv` in your 
   terminal
3. Run the virtual environment
  - Windows: Run `.\venv\Scripts\activate.bat`
  - Mac: Run `source venv/bin/activate`
4. install dependencies by running `pip install -r requirements.txt` in the virtual environment

### OpenAI setup
1. Create a .env file in your root folder
2. Put `OPENAI_API_KEY="your-open-ai-api-key"` in your root folder

## Development
Run this service by running `uvicorn main:app --reload`

The server will be available through http://127.0.0.1:8000/

You cam visit http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc to see automatic API 
documentation while the server is running

## Learn More

This project uses [FastAPI](https://fastapi.tiangolo.com/)
