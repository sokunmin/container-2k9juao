
# Build image commands

Build server image

```bash
$ docker build -t server-image -f server.Dockerfile .
```

Build client image

```bash
$ docker build -t client-image -f client.Dockerfile .
```

# Create bridge network

```bash
$ docker network create mynet
```

# Run server container

```bash
$ docker run --rm --name server-container --network mynet server-image
```

# Run client container

```bash
$ docker run --rm --name client-container --network mynet client-image
```