# DAISYXMUSIC- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith

import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCOmf87Hud-PXuDupIzEk4Yr8GPMTrt6NjbQMBg88NujtLbgrsztCMBF3rPwQYDVQsF7UYZLfmsZkGc1JeRobyNMflkqcMi36UuLs9c0b0uPPxnc7aywK4GY0zwnQLTbc4sylgW79n9kVtdkZjnU4eLgTBsQwJKe1ojZxQCaY32-tyVdlh06COjJUPSU-IgzO46S9hMUWOS1uOWpYxRYSDltyGubdEZiYCNuLzT-0NrJZLQuhkPhT8RLMSsVqk3xzgWVoWa2BClFajvijFnH0pNYQVR73YyyTnsUqNd9QSyZnXQgNb7L8ckom8IGb5IKxnzOLT3Hc7FYJ7JgTo2hN_6RMcZRQA")
BOT_TOKEN = getenv("1998824533:AAGHkte-cFBNmyNR-4uvW6er4Uw2yQBE5BE")
BOT_NAME = getenv("SHAGGY MUSIC PLAYER")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DaisyXupdates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/795482723c8accc2cf623.jpg")
admins = {Mr SHAGGY}
API_ID = int(getenv("6065291", "6065291"))
API_HASH = getenv("dc7873c0a5c737af4356d4f245fe696d")
BOT_USERNAME = getenv("@shaggy_music_player_bot")
ASSISTANT_NAME = getenv("SHAGGY MUSIC PLAYER ASSISTANT", "DaisyXhelper")
SUPPORT_GROUP = getenv("519164039", "DaisySupport_Official")
PROJECT_NAME = getenv("PROJECT_NAME", "DaisyXMusic v5")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/TeamDaisyX/DaisyXMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
