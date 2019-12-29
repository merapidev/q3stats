import os
import re

def start():
    print("Start")

    regex = re.compile('^[0-9]{4}.[0-9]{2}.[0-9]{2}_#[0-9]+')

    with os.scandir('files/') as files:
        for file_with_logs in files:
            
            if not regex.match(file_with_logs.name):
                continue
            
            print(file_with_logs.name)

            with open(file_with_logs) as file_pointer:
                for line in file_pointer:
                    
                    if 'Com_TouchMemory' in line:
                        print('NEW GAME==================================')
                        continue

                    if 'RE_Shutdown' in line:
                        print('END GAME==================================')
                        continue

                    if '^7' in line:
                        print(line)



if __name__ == "__main__":

    start()
