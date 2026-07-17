import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")
EXPECTED_KEYS = {"total_requests", "unique_ips", "top_path"}


def load_report():
    return json.loads(REPORT_PATH.read_text(encoding="utf-8"))


def test_report_exists_and_is_valid_json():
    """Success criterion 1: /app/report.json exists and contains valid JSON."""
    assert REPORT_PATH.is_file(), "missing /app/report.json"
    try:
        load_report()
    except json.JSONDecodeError as exc:
        raise AssertionError("/app/report.json is not valid JSON") from exc


def test_report_has_exact_required_keys():
    """Success criterion 2: the JSON object contains exactly the required keys."""
    report = load_report()
    assert isinstance(report, dict), "report must be a JSON object"
    assert set(report) == EXPECTED_KEYS, "report has missing or unexpected keys"


def test_total_requests_matches_log():
    """Success criterion 3: total_requests is the integer count of non-empty log entries."""
    report = load_report()
    assert type(report["total_requests"]) is int, "total_requests must be an integer"
    assert report["total_requests"] == 6, "total_requests must equal 6"


def test_unique_ips_matches_log():
    """Success criterion 4: unique_ips is the integer count of distinct client IPs."""
    report = load_report()
    assert type(report["unique_ips"]) is int, "unique_ips must be an integer"
    assert report["unique_ips"] == 3, "unique_ips must equal 3"


def test_top_path_matches_log():
    """Success criterion 5: top_path is the most frequently requested path."""
    report = load_report()
    assert type(report["top_path"]) is str, "top_path must be a string"
    assert report["top_path"] == "/index.html", "top_path must equal /index.html"
