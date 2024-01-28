from fastapi import FastAPI
import multiprocessing
import time
import uvicorn
import psutil

app = FastAPI()

@app.get("/")
def read_root():
    cpu_percent = psutil.cpu_percent()
    return {"message": "Hello World", "CPU Usage": f"{cpu_percent}%"}


@app.get("/add_cpu_load")
def add_cpu_load():
    # Simulate CPU load
    with multiprocessing.Pool() as pool:
        result = pool.map(simulate_work, range(10))
    return {"status": "CPU load added successfully"}


def simulate_work(_):
    # Simulate CPU-bound work
    start_time = time.time()
    while time.time() - start_time < 30:  # Simulate 30 seconds of CPU load
        _ = 2 ** 1000  # Perform a heavy computation
    return "done"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)