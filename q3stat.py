import datetime
import os
import re

import click
from pymongo import MongoClient

@click.group()
def main():
    pass

@main.command()
def load():
    """Load new log files to DB"""
    print("Load logs")

    client = MongoClient('localhost', 27017)
    q3stat_db = client['q3stat']
    raw_logs = q3stat_db['raw-logs']

    regex = re.compile('^[0-9]{4}.[0-9]{2}.[0-9]{2}_#[0-9]+')

    with os.scandir('files/') as files:
        for log_file in files:

            if not regex.match(log_file.name):
                continue

            with open(log_file) as file_pointer:
                load_games(file_pointer, log_file, raw_logs)


def load_games(file_pointer, log_file, raw_logs):
    raw_log_game = {}
    for line in file_pointer:

        if is_start_game(line):
            raw_log_game = {
                "filename": log_file.name,
                "date": datetime.datetime.strptime(log_file.name[:10], "%Y.%m.%d"),
                "entries": []
            }
            continue

        if is_end_game(line):
            if not raw_log_game:
                continue
            raw_logs.insert_one(raw_log_game)
            raw_log_game = {}
            continue

        if is_game(line):
            raw_log_game["entries"].append(line)


def is_game(line):
    return "^7" in line


def is_end_game(line):
    return "RE_Shutdown" in line


def is_start_game(line):
    return "Com_TouchMemory" in line


if __name__ == "__main__":
    main()
