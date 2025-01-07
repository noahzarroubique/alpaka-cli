#!/usr/bin/env bash
cd "$(dirname "$0")"
source venv/bin/activate
date >> log.log
python main.py >> log.log