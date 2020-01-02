import os
import re
import datetime
from pymongo import MongoClient


def load_logs():
    print("Load logs")

    client = MongoClient('localhost', 27017)
    q3stat_db = client['q3stat']
    raw_logs = q3stat_db['raw-logs']

    regex = re.compile('^[0-9]{4}.[0-9]{2}.[0-9]{2}_#[0-9]+')

    with os.scandir('files/') as files:
        for file_with_logs in files:

            if not regex.match(file_with_logs.name):
                continue

            raw_log_game = {}

            print(file_with_logs.name)
            print(raw_log_game)

            with open(file_with_logs) as file_pointer:
                for line in file_pointer:

                    if "Com_TouchMemory" in line:
                        raw_log_game = {
                            "filename": file_with_logs.name,
                            "date": datetime.datetime.strptime(file_with_logs.name[:10], "%Y.%m.%d"),
                            "entries": []
                        }
                        continue

                    if "RE_Shutdown" in line:
                        if not raw_log_game:
                            continue
                        raw_logs.insert(raw_log_game)
                        raw_log_game = {}
                        continue

                    if "^7" in line:
                        raw_log_game["entries"].append(line)


if __name__ == "__main__":

    load_logs()
