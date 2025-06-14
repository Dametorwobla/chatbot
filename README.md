# Mental Health Support Chatbot 🤖

A Streamlit-based chatbot that provides mental health support and guidance using OpenAI's GPT model. This application offers a safe space for users to discuss their mental health concerns and receive supportive, non-medical advice.

## Features 🌟

- Interactive chat interface
- Real-time responses using OpenAI's GPT model
- Mental health symptom assessment
- Non-medical advice and support
- Wellness tips and guidance
- Emergency resource information
- Privacy-focused design

## Tech Stack 💻

- **Frontend**: Streamlit
- **AI Model**: OpenAI GPT-3.5 Turbo
- **Language**: Python 3.11+
- **Environment Management**: Python Virtual Environment
- **API Integration**: OpenAI API

## Prerequisites 📋

- Python 3.11 or higher
- OpenAI API key
- pip (Python package installer)

## Installation 🚀

1. Clone the repository:
```bash
git clone https://github.com/dametorwobla/chatbot.git
cd chatbot
```

2. Create and activate a virtual environment:
```bash
# On macOS/Linux
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```env
OPENAI_API_KEY=your_api_key_here
```

## Project Structure 📁

```
chatbot/
├── .env                    # Environment variables
├── .gitignore             # Git ignore file
├── README.md              # Project documentation
├── requirements.txt       # Project dependencies
├── src/
│   ├── __init__.py       
│   ├── config.py         # Configuration settings
│   ├── models/
│   │   ├── __init__.py   
│   │   └── openai_client.py
│   ├── utils/
│   │   ├── __init__.py  
│   │   └── chat_utils.py
│   └── app.py
└── tests/
    └── __init__.py       
```


## Usage 🎮

1. Start the application:
```bash
streamlit run src/app.py
```

2. Open your web browser and navigate to:
http://localhost:8501


3. Start chatting with the bot!

## Important Notes ⚠️

- This chatbot is not a replacement for professional medical advice
- Always consult healthcare providers for medical concerns
- The chatbot provides general support and guidance only
- Your privacy is important - no chat history is stored permanently

## Emergency Resources 🚑

If you're experiencing a mental health emergency:
- Call emergency services: 911
- National Suicide Prevention Lifeline: 988
- Crisis Text Line: Text HOME to 741741

## Security 🔒

- API keys are stored in environment variables
- No sensitive data is stored
- All communications are encrypted
- Regular security updates are implemented

## Contributing 🤝

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## Testing 🧪

Run tests using pytest:
```bash
pytest tests/
```

## Deployment 🚀

The application can be deployed on various platforms:
- Streamlit Cloud
- Heroku
- AWS
- Google Cloud Platform

Remember to set up the environment variables on your chosen platform.

## License 📝

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- OpenAI for providing the GPT model
- Streamlit for the web framework
- All contributors and supporters of the project

## Contact 📧

For any questions or concerns, please open an issue in the GitHub repository.

---

**Disclaimer**: This chatbot is for educational and portfolio purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.