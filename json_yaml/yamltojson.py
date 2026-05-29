#Your team uses YAML configs (Kubernetes, Ansible). You need to convert them to JSON.


import yaml

# Read YAML (similar to json.load)
with open("config1.yaml", "r") as file:
    config = yaml.safe_load(file)

    print(config)


print(type(config))
