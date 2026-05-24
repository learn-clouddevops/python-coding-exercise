#Given a multi-line log string, count occurrences of each log level (INFO, WARN, ERROR).
import os

filepath = os.path.join(os.path.dirname(__file__),"loglevel.txt")



try:
    if os.path.isfile(filepath):
        with open(filepath, "r") as file:


            infocount =0
            errorcount =0
            warncount=0
            for line in file:
                if "INFO" in line:
                    infocount += 1

                elif "ERROR" in line:
                    errorcount += 1

                elif "WARN" in line:
                    warncount += 1
            print(f"INFO: {infocount}, ERROR: {errorcount}, WARN: {warncount}")        
                    

except FileNotFoundError:
        print("incorrect file") 
