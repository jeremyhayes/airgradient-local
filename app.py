from flask import Flask, request

app = Flask(__name__)

@app.get("/")
def get_index():
    return "<p>Hello, World!</p>"

@app.post("/sensors/airgradient:<chip_id>/measures")
def post_sensor_measures(chip_id):
    # TODO store this for later prometheus scrape
    print(f"""DEBUG
        chip_id={chip_id},
        wifi={request.json['wifi']},
        rco2={request.json['rco2']},
        pm02={request.json['pm02']},
        atmp={request.json['atmp']},
        rhum={request.json['rhum']},
        """, flush=True)

    return ('', 201)
