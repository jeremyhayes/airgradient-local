# airgradient-local

Minimal web service to capture data from [Airgradient devices](https://www.airgradient.com/open-airgradient/) and expose as Prometheus-formatted metrics.

## Usage

### Docker
```sh
$ docker run \
   --name airgradient \
   -p 5000:5000 \
   ghcr.io/jeremyhayes/airgradient-local:v0.0.1
```

### Docker Compose
```yml
version: '3.8'

services:

  airgradient:
    image: ghcr.io/jeremyhayes/airgradient-local:v0.0.1
    ports:
      - 5000:5000
```