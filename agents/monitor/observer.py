import requests, time, os


def check_health(url="http://localhost:5000"):
    for _ in range(5):
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return "Healthy"
        except Exception:
            time.sleep(2)
    return "Unhealthy"


if __name__ == "__main__":
    status = check_health()
    os.makedirs("artifacts", exist_ok=True)
    with open("artifacts/report.md", "w") as f:
        f.write(f"# Observer Report\n\nStatus: {status}\n")
