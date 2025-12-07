<div align="center">

# 🔍 Product Jobs Hunter

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://core.telegram.org/bots)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT-green.svg)](https://platform.openai.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

### Smart Product Manager Job Parser from Telegram with GPT Analysis

English | [Русский](README.md)

</div>

## 👨‍💻 Author

**JhonnyAxe**
- Telegram: [@jhonnyaxe](https://t.me/jhonnyaxe)
- GitHub: [github.com/JhonnyAxe](https://github.com/JhonnyAxe)

## 🌟 About

Product Jobs Hunter is a smart tool for monitoring and analyzing Product Manager vacancies in Telegram channels. It uses GPT to determine the relevance of vacancies and automatically sends notifications about new job offers.

### ✨ Features
- 🤖 **AI-Powered Analysis** - Uses GPT to evaluate Product Manager relevance
- 🔄 **Real-time Updates** - Instant notifications about new vacancies
- 📊 **Smart Filtering** - Automatic salary and requirements detection
- 💾 **Excel Export** - Save all vacancies in a convenient format
- 🔍 **Smart Search** - Recognition of various Product Manager/Owner wording

## 💻 Project Files

📄 `new_vacancies_parser_channels.py`
- Main monitoring script
- Tracks new messages
- Launches analysis and notification sending

📄 `parse_channels.py`
- Channel parsing module
- Contains message analysis logic
- Extracts contacts and salaries

📄 `product_channels.py`
- List of monitored channels
- Add new channels here

📄 `send_existing_vacancies.py`
- Send existing vacancies
- Useful for first launch

📄 `telegram_notifier.py`
- Send notifications to Telegram
- Message formatting

📄 `stop_words.py`
- Words for filtering
- Helps filter out irrelevant messages (agencies, marketing roles, freelance)

## 🔑 API Keys Setup

1. **Telegram API**
   - Go to https://my.telegram.org
   - Create an application
   - Get `API_ID` and `API_HASH`

2. **OpenAI API**
   - Register at https://platform.openai.com
   - Create API key

3. **Create `.env` file:**
```env
API_ID="your_api_id"
API_HASH="your_api_hash"
PHONE="your_phone"
OPENAI_API_KEY="your_openai_api_key"
BOT_TOKEN="your_bot_token"
RECIPIENT_CHAT_ID="your_target_user_chat_id"
PRODUCT_FILE="product_vacancies.xlsx"
```

4. **Direct message setup**
   1. Create a bot via [@BotFather](https://t.me/BotFather) and copy the `BOT_TOKEN`.
   2. Send any message to your bot to open the dialog.
   3. Open `https://api.telegram.org/bot<BOT_TOKEN>/getUpdates` in a browser and find your `chat.id` in the response.
   4. Put this `chat.id` into the `RECIPIENT_CHAT_ID` variable in `.env`.

## 💻 Installation

1. Clone the repository:
```bash
git clone https://github.com/JhonnyAxe/ProductJobsHunter.git
cd ProductJobsHunter
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure `.env` as described above

4. Start monitoring:
```bash
python new_vacancies_parser_channels.py
```

## 💾 Results

All found vacancies:
- Saved to `product_vacancies.xlsx`
- Sent to your direct chat with the bot

## 🔄 How It Works

1. 📱 Connects to specified Telegram channels
2. 🔍 Searches for messages with Product Manager/Owner keywords
3. 🤖 Analyzes text through GPT
4. 📊 Extracts important information
5. 📬 Sends notification if a vacancy is found
6. 💾 Saves to Excel for history

## ⚙️ Configuration

All settings are stored in three files:
- `.env` - API keys and main settings
- `product_channels.py` - list of channels to monitor
- `stop_words.py` - words for filtering

## 🔒 Security

- Never publish your `.env` file
- Follow Telegram API limitations
- Use reasonable delays between requests

## 📝 License

MIT License © 2024 [JhonnyAxe](https://t.me/jhonnyaxe)

## 👏 Acknowledgments

Developed by [JhonnyAxe](https://t.me/jhonnyaxe)

If you have any questions or suggestions, contact me on Telegram!
