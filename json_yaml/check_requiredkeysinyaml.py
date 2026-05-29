

# Problem 3: Check if Config Has All Required Keys
import yaml
required_keys = ["app_name", "port", "database.port", "log_level"]

def key_exist(config,key):
        parts = key.split('.')
        # print(config)
        # print(key)

        current = config
        for part in parts:
               
            if isinstance(current,dict) and part in current:
                  current = current[part]
               
                
            else:
                return False  # Key not found!
    
        return True 


def check_required_keys(filename):
        with open(filename, "r") as file:

            config = yaml.safe_load(file)
            print("Full config:", config)
            print("Type:", type(config))
            print("Database:", config.get('database'))

            missing = []
            for key in required_keys:
                    # if key not in config:
                    #     missing.append(key)
                    if not key_exist(config,key):
                           missing.append(key)

            return missing
filename= "config1.yaml"

result = check_required_keys(filename)
print(f"Missing keys: {result}")
