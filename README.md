# Telegram Bot Guard

A Telegram bot that automatically prevents unauthorized bots from being added to groups. Only admins and group owners can add bots to the group.

## Features

- 🤖 Automatically detects when bots are added to the group
- 🛡️ Kicks bots that are added by regular members
- 👑 Allows admins and group owners to add bots normally
- 📢 Sends notification messages when removing bots
- ⚡ Fast and lightweight

## Requirements

- Python 3.7 or higher
- python-telegram-bot library (v20.0+)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/telegram-bot-guard.git
cd telegram-bot-guard
Install required dependencies:
pip install python-telegram-bot
Or use requirements.txt:
pip install -r requirements.txt
Setup
Create a bot:
Go to @BotFather on Telegram
Send /newbot and follow the instructions
Copy the bot token you receive
Configure the bot:
Open bot.py
Replace YOUR_BOT_TOKEN_HERE with your actual bot token:
BOT_TOKEN = "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"
Run the bot:
python bot.py
Add to your group:
Add the bot to your Telegram group
Make the bot an admin with the following permissions:
✅ Ban users
That's it! The bot is now protecting your group
How It Works
The bot monitors all new members joining the group
When a bot is added, it checks who added it
If added by a regular member → the bot is kicked
If added by an admin/owner → the bot is allowed to stay
A notification message is sent when a bot is removed
Configuration
You can customize the bot's behavior by modifying these settings in bot.py:
# Notification message when a bot is removed
await message.reply_text(
    f"Bot @{new_member.username or new_member.first_name} was removed.\n"
    f"Only admins can add bots to this group."
)
Permissions Required
The bot needs the following admin permissions:
Ban users - Required to kick unauthorized bots
Example Usage
Regular Member: *adds a bot to the group*
Bot Guard: "Bot @ExampleBot was removed. Only admins can add bots to this group."

Admin: *adds a bot to the group*
Bot Guard: *allows the bot to stay*
Troubleshooting
Bot doesn't kick other bots:
Make sure the bot has admin permissions with "Ban users" enabled
Verify your bot token is correct
Check that the bot is running
Bot kicks bots added by admins:
This shouldn't happen. If it does, check the Telegram API permissions
Ensure the admin has proper admin rights in the group
Requirements.txt
Create a requirements.txt file:
python-telegram-bot>=20.0
License
This project is licensed under the MIT License - see the LICENSE file for details.
Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
Support
If you encounter any issues or have questions:
Open an issue on GitHub
Contact: [your-email@example.com]
Disclaimer
This bot is provided as-is. Make sure to comply with Telegram's Terms of Service and Bot API terms when using this bot.
Author
Your Name - @mkarami313
Acknowledgments
Built with python-telegram-bot
Inspired by the need for better group management on Telegram
⭐ If you find this project useful, please consider giving it a star!
You can also create these additional files for a complete repository:

**requirements.txt:**
python-telegram-bot>=20.0
**LICENSE (MIT License):**
MIT License
Copyright (c) 2025 [mahdi]
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
**.gitignore:**
Python
pycache/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
Bot token (security)
config.py
.env
IDE
.vscode/
.idea/
*.swp
*.swo
*~
OS
.DS_Store
Thumbs.db
