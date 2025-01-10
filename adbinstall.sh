#!/usr/bin/env bash
cd "$(dirname "$0")"
source venv/bin/activate
echo >> log.log
date >> log.log
PATH=$PATH:/mnt/c/Users/noahz/AppData/Local/Android/Sdk/platform-tools
python main.py >> log.log 2>&1