docker build -t yaml_parser .

docker run --rm -v ./test_yaml.yml:/usr/src/app/test_yaml.yml yaml_parser
