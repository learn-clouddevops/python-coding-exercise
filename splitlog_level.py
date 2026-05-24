#Parse a line like 2024-01-15 10:23:45 ERROR Disk full into a dict with date, time, level, message.

line ="2024-01-15 10:23:45 ERROR Disk full error . Please increase the disk"

#using generator
import os

def iterate_on_file(filepath):
    
    try:
      # filename = os.path.basename(filepath)
      if os.path.isfile(filepath):
        with open(filepath, "r") as file:
            for line in file:
  

            # return line


                parts = line.split(maxsplit=3)   
                data = {
                   "date": parts[0],
                   "time": parts[1],
                   "level": parts[2],
                   "message": parts[3]

                }

               #  print(data)  
                yield data


      else:
         print("filenot found") 
    except FileNotFoundError:
       print("No FILE EXIST")



       


filepath = os.path.join(os.path.dirname(__file__),"loglevel.log")

if __name__ == "__main__":
   logfile = iterate_on_file(filepath)
#    print(logfile)
   for item in logfile:
      print(item)
