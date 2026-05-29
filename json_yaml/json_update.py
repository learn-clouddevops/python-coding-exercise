## You have a JSON config file. Load it, change a value, save it back.



# config.json contains:


# Task: Change "debug" to true and "port" to 9090, save back
''''''
import os
import json

filename = "config.json"

def changejson(filename):
    try:
        print("Current directory:", os.getcwd())
        print("Full path:", os.path.abspath(filename))
        if not os.path.isfile(filename):
            return False
        with open(filename, "r") as file:
            config = json.load(file)

            print("before:", config)    
    
                    # Step 2: Modify values
            config['debug'] = True
            config['port'] = 9094
        print("After:", config)    

        with open(filename,"w") as file:
            json.dump(config, file , indent=2)    

        print(type(config))

        return config    
            

    except FileNotFoundError:
        print("No FILE EXIST")

result= changejson(filename)        
print(result)


    

