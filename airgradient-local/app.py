from flask import Flask, request, Response
import prometheus_client as prom

app = Flask(__name__)

# remove default collectors
prom.REGISTRY.unregister(prom.GC_COLLECTOR)
prom.REGISTRY.unregister(prom.PLATFORM_COLLECTOR)
prom.REGISTRY.unregister(prom.PROCESS_COLLECTOR)

# define airgradient metrics
gauge_wifi = prom.Gauge("airgradient_wifi", "", ["chip_id"])
gauge_rco2 = prom.Gauge("airgradient_rco2", "", ["chip_id"])
gauge_pm02 = prom.Gauge("airgradient_pm02", "", ["chip_id"])
gauge_atmp = prom.Gauge("airgradient_atmp", "", ["chip_id"])
gauge_rhum = prom.Gauge("airgradient_rhum", "", ["chip_id"])

@app.get("/")
def get_index():
    return "<p>Hello, World!</p>"

@app.get("/metrics")
def get_metrics():
    return Response(prom.generate_latest(), mimetype=prom.CONTENT_TYPE_LATEST)

@app.post("/sensors/airgradient:<chip_id>/measures")
def post_sensor_measures(chip_id):
    labels = {
        "chip_id": chip_id
    }

    gauge_wifi.labels(**labels).set(request.json['wifi'])
    gauge_rco2.labels(**labels).set(request.json['rco2'])
    gauge_pm02.labels(**labels).set(request.json['pm02'])
    gauge_atmp.labels(**labels).set(request.json['atmp'])
    gauge_rhum.labels(**labels).set(request.json['rhum'])

    return ('', 201)
