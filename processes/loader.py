import datetime
import os
import re

from common.collection import Collection
from .base import Process as BaseProcess


class Loader(BaseProcess):

    def execute(self):

        self.storage.set_up_collection(Collection.RAW_DATA)

        regex = re.compile('^[0-9]{4}.[0-9]{2}.[0-9]{2}_#[0-9]+')

        # @TODO mark and skip processed files

        with os.scandir(self.config.files_directory) as files:
            for log_file in files:

                if not regex.match(log_file.name):
                    continue

                with open(log_file) as file_pointer:
                    self.load_contest(file_pointer, log_file)

    def load_contest(self, file_pointer, log_file):

        raw_log_game = {}
        for line in file_pointer:

            if self.__is_start_game(line=line):
                raw_log_game = {
                    "filename": log_file.name,
                    "date": datetime.datetime.strptime(log_file.name[:10], "%Y.%m.%d"),
                    "entries": []
                }
                continue

            if self.__is_end_game(line=line):
                if not raw_log_game:
                    continue
                self.storage.insert_one(document=raw_log_game)
                raw_log_game = {}
                continue

            if self.__is_game(line=line) and not self.__is_skippable(line=line):
                line = line.replace('Killer is Back !!!', 'Killer')
                raw_log_game["entries"].append(line)

    def __is_game(self, line):
        return "^7" in line

    def __is_skippable(self, line):
        return self.__is_player_message(line=line) \
               or self.__is_capture_the_flag_message(line=line) \
               or self.__is_hit_the_flaglimit(line=line) \
               or self.__is_connected_message(line=line) \
               or self.__is_disconnected_message(line=line) \
               or self.__is_entered_the_game(line=line) \
               or self.__is_timeout(line=line)

    def __is_player_message(self, line):
        return "^2" in line

    def __is_capture_the_flag_message(self, line):
        return "flag" in line

    def __is_hit_the_flaglimit(self, line):
        return "hit the fraglimit" in line

    def __is_connected_message(self, line):
        return "connected" in line

    def __is_disconnected_message(self, line):
        return "disconnected" in line

    def __is_entered_the_game(self, line):
        return "entered the game" in line

    def __is_timeout(self, line):
        return "timed out" in line

    def __is_end_game(self, line):
        return "RE_Shutdown" in line

    def __is_start_game(self, line):
        return "Com_TouchMemory" in line
