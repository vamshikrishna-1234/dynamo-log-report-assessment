import json


def test_total_requests():
    """Criterion 1: total_requests equals the number of requests in the log."""
    with open("/app/report.json") as report:
        data = json.load(report)
    assert data.get("total_requests") == 6, "total_requests is incorrect"


def test_unique_ips():
    """Criterion 2: unique_ips equals the number of distinct client IPs."""
    with open("/app/report.json") as report:
        data = json.load(report)
    assert data.get("unique_ips") == 3, "unique_ips is incorrect"


def test_top_path():
    """Criterion 3: top_path is the single most frequently requested path."""
    with open("/app/report.json") as report:
        data = json.load(report)
    assert data.get("top_path") == "/index.html", "top_path is incorrect"
