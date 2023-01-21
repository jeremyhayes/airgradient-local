# airgradient-local

Local [Airgradient](https://www.airgradient.com/open-airgradient/) setup, in two parts
1. Arduino sketch, based on the official `DIY_BASIC` example
1. Docker service to capture data and expose Prometheus-formatted metrics

## Usage

### Arduino

The AirGradient device is an Arduino microprocessor. It runs a tiny program that continuously reads data from its sensors and sends them to a configured location. By default this is Airgradient's hosted service, but we'll run our own.

1. Update configuration as needed
  - Set `APIROOT` to your target server.
  - Set `ssid`/`password` for your wifi setup.
1. Setup Arduino IDE and the necessary configuration per [AirGradient's instructions](https://www.airgradient.com/open-airgradient/instructions/basic-setup-skills-and-equipment-needed-to-build-our-airgradient-diy-sensor/)
1. Flash the updated sketch onto your Airgradient device

### Hub Service

The service acts as a hub that receives metrics from one or more Airgradient devices and exposes them in a format that can then be scraped by a Prometheus server for Grafana visualization.

The service itself runs as a Docker image, which you can either run independently:

```sh
$ docker run \
   --name airgradient \
   -p 5000:5000 \
   ghcr.io/jeremyhayes/airgradient-local:latest
```

...or via compose/swarm (preferred), perhaps as part of a larger service configuration:

```yml
version: '3.8'

services:

  airgradient:
    image: ghcr.io/jeremyhayes/airgradient-local:latest
    ports:
      - 5000:5000
```
