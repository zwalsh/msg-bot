#!/usr/bin/bash
cd "$(dirname "$0")"
export MSG_BOT_MSG_URL=https://www.zachwal.sh/msg.txt;
python3 main.py fetch;
