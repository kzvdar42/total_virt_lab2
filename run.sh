docker build . -t rabbit_test:0.42
docker run --rm -d --name rabbit_test -i rabbit_test:0.42