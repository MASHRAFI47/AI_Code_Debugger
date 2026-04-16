
# AI Code Debugger

A smart web application that allows users to upload screenshots of code errors and get instant debugging help using the Gemini API. The app analyzes the image, detects issues in the code, and provides either helpful hints or complete solutions with corrected code.




## Features

- 📸 Upload code error screenshots (JPG, JPEG, PNG)
- 🤖 AI-powered debugging using Gemini API
- 💡 Two modes:
    * Hints (guidance without full solution)
    * Solution with Code (complete fix)
- ⚡ Fast and interactive UI with Streamlit
- ⏳ Loading indicators using spinners
- ⚠️ Proper error handling for missing inputs
- 🔐 Secure API key management using .env

## Demo

https://ai-code-debug.streamlit.app/


## 🛠 Tech Stack
Javascript, HTML, CSS...

- Frontend/UI: Streamlit
- Backend Logic: Python
- AI Model: Gemini API
- Image Processing: Pillow
- Environment Management: python-dotenv
## Run Locally

Clone the project

```bash
git clone https://github.com/MASHRAFI47/AI_Code_Debugger.git
```

Go to the project directory

```bash
cd ai_code_debugger
```

Install dependencies

```bash
pip install streamlit
pip install google-genai
pip install python-dotenv
```

Start the server

```bash
streamlit run app.py
```


## 📸How It Works

- Upload a screenshot of your code error
- Select either Hints or Solution with Code
- Click Debug Code
- Get AI-generated explanation and fix instantly


## ⚠️Notes

- Make sure your screenshots are clear and readable
- API key is required for the app to function
- Generate API from here https://aistudio.google.com/api-keys
## Authors

- [@MASHRAFI47](https://www.github.com/MASHRAFI47)


## Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.


## License



[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


