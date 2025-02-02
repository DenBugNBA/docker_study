import yaml

if __name__ == "__main__":
    with open("test_yaml.yml") as f:
        templates = yaml.safe_load(f)
    print(templates)
