# Jeanne Discord Bot

## Overview

Jeanne is a multipurpose Discord bot built with discord.py. It provides moderation, server management, levelling, currency/economy, fun commands, reaction GIFs, NSFW content, AI chat, image galleries, welcome/goodbye messages, and more. The bot uses slash commands, supports multi-language responses (English, French, German/Dutch), and integrates with several third-party services. It runs as an auto-sharded bot and stores data in a local SQLite database.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Bot Framework
- **Library:** discord.py with `AutoShardedBot` for horizontal scaling across Discord shards
- **Entry point:** `jeanne.py` — initializes the bot, loads all cogs/events dynamically from `./cogs` and `./events` directories, sets up the translation system, and syncs the command tree
- **Command style:** Primarily slash commands (`app_commands`), with a legacy prefix (`J!`, `j!`, `Jeanne`, `jeanne`) used only for owner/developer commands

### Project Structure
- **`cogs/`** — Slash command groups (fun, moderation, manage, levelling, currency, help, info, inventory, reactions, utilities, hentai, image, owner, error handling, command logging). Each cog acts as a thin dispatcher that checks the user's locale and delegates to the appropriate language module.
- **`events/`** — Event listeners and background tasks (message XP processing, welcome/goodbye handling, Top.gg webhook/stats, softban expiry, reminders, suspensions)
- **`languages/`** — Localized response modules organized by language (`en/`, `fr/`, `de/`). Each language folder mirrors the cog structure. The `Translator.py` file handles Discord's built-in localization for command names/descriptions/parameters.
- **`assets/`** — Shared UI components (`components.py`), image fetchers (`images.py`), profile card generator (`generators/profile_card.py`), blackjack game logic (`blackjack_game.py`), dictionary lookup (`dictionary.py`), and AI chat (`AI/openai.py`)
- **`functions.py`** — Core business logic classes: `DevPunishment`, `Levelling`, `Currency`, `Inventory`, `Moderation`, `Welcomer`, `Manage`, `Confess`, `Reminder`, `Hentai`, etc. All database operations go through this file.
- **`config.py`** — Loads environment variables and initializes the SQLite connection and Tenor API URLs
- **`db_check.py`** — Startup script that ensures all required SQLite tables exist, creating missing ones

### Localization Pattern
The bot uses a delegation pattern for i18n. Each cog checks `ctx.locale.value` (or `ctx.guild.preferred_locale.value` for server-level locale) and instantiates the corresponding language class from `languages/{lang}/`. Command names and descriptions use `locale_str` (aliased as `T`) with translations defined in `languages/Translator.py`.

### Database
- **SQLite** (`database.db`) with Python's built-in `sqlite3` module, `autocommit=True`
- Key tables include: `currency`, `reminderData`, `softbannedMebers`, `botbannedData`, `serverxpData`, `globalxpData`, `userWallpaperInventory`, confession data, welcomer config, modlog config, level settings, and more
- `db_check.py` handles schema migrations by checking for missing tables at startup
- No ORM is used; raw SQL queries throughout `functions.py`

### Logging
- Command usage logged to `commands.xlsx` (pandas/openpyxl)
- Errors logged to `errors.xlsx` (pandas/openpyxl)
- Level cooldowns stored in JSON

### Profile Card Generation
- Uses Pillow (PIL) to generate profile card images with user avatar, XP bar, level, badges, and custom backgrounds
- Backgrounds and badges are purchasable through the in-game currency system

### AI Integration
- Uses OpenAI-compatible API via OpenRouter (`https://openrouter.ai/api/v1`)
- Per-server conversation history stored as text files in `assets/AI/history/`
- System prompt gives the bot a personality (Jeanne from Fate series)

## External Dependencies

### Third-Party Services & APIs
- **Discord API** — via discord.py (`AutoShardedBot`, slash commands, sharding)
- **Top.gg** — Bot listing, vote tracking, webhook for vote rewards, stats posting (`topggpy` / `DBLClient`)
- **discord.bots.gg** — Secondary bot listing, stats posting via REST API
- **Tenor API** — Reaction GIFs (hug, slap, pat, kiss, etc.)
- **OpenRouter/OpenAI** — AI chatbot responses
- **Gelbooru & Rule34** — NSFW image fetching (API key + user ID auth)
- **OpenWeatherMap** — Weather command (`WEATHER` env var)
- **Catbox** — File/image hosting (uses hash-based auth)
- **Dictionary API** — `dictionaryapi.dev` for word definitions
- **Discohook** — Referenced for embed JSON generation (external tool, not an API integration)

### Key Python Packages
- `discord.py` — Core bot framework
- `aiohttp` — Async HTTP requests
- `Pillow` — Image generation for profile cards
- `pandas` / `openpyxl` — Excel-based command and error logging
- `humanfriendly` — Time parsing and formatting
- `topggpy` — Top.gg SDK
- `reactionmenu` — Paginated embed menus
- `py-expression-eval` — Calculator/math expression evaluation
- `python-dotenv` — Environment variable loading
- `jishaku` — Developer/debug extension
- `openai` — OpenAI client (pointed at OpenRouter)
- `markdown` — Markdown to HTML conversion for AI context

### Environment Variables Required
All secrets are loaded via `.env` file: `token`, `weather_api`, `topgg`, `topgg_auth`, `db_auth`, `report_webhook`, `botban_webhook`, `tenor`, `client_key`, album paths (jeanne, saber, wallpaper, medusa, animeme, neko, morgan, kitsune), `catbox_hash`, `badges_album`, `status`, `GELBOORU_API_KEY`, `GELBOORU_USER_ID`, `RULE34_API_KEY`, `RULE34_USER_ID`, `OPENAI_API_KEY`