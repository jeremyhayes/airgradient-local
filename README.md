# airgradient-local-prometheus

Minimal web service to capture data from [Airgradient devices](https://www.airgradient.com/open-airgradient/) and expose as Prometheus-formatted metrics.

## Usage

### Docker
```sh
$ docker run \
   --name airgradient-local-prometheus \
   -p 5000:5000 \
   ghcr.io/jeremyhayes/airgradient-local-prometheus:v0.0.1
```

### Docker Compose
```yml
version: '3.8'

services:

  infinitude-prometheus:
    image: ghcr.io/jeremyhayes/airgradient-local-prometheus:v0.0.1
    ports:
      - 5000:5000
```