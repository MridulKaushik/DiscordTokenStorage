# Django Discord Bot Authentication App

This Django application provides an authentication flow to obtain and store Discord bot access tokens using the OAuth2 authorization code grant. The access token is obtained by exchanging the authorization code provided during the authorization process.

## Getting Started

### Prerequisites

- Python (3.6 or higher)
- Django
- Requests library
- Discord.py library


### Discord Bot
The Discord bot logic is implemented in discord_bot.py. This script interacts with the Discord API using the discord.py library.

Prerequisites
Python (3.6 or higher)
Discord.py library
Installation
Install the required Python packages:

```bash
pip install discord
```

Replace 'YOUR_BOT_TOKEN' in discord_bot.py with your actual Discord bot token.

### Important Notes
- Keep your Discord bot token secure and do not share it publicly.
- Ensure that the Django development server is running when interacting with the Discord bot.
