import json
import re
from collections import Counter
from pathlib import Path

LOG_PATH = Path("/app/access.log")
REPORT_PATH = Path("/app/report.json")
REQUEST_PATTERN = re.compile(r'"[A-Z]+\s+(\S+)\s+HTTP/[^\"]+"')


def main() -> None:
    total_requests = 0
    unique_ips: set[str] = set()
    path_counts: Counter[str] = Counter()

    for raw_line in LOG_PATH.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue

        total_requests += 1
        unique_ips.add(line.split(maxsplit=1)[0])

        match = REQUEST_PATTERN.search(line)
        if match:
            path_counts[match.group(1)] += 1

    top_path = path_counts.most_common(1)[0][0] if path_counts else ""
    report = {
        "total_requests": total_requests,
        "unique_ips": len(unique_ips),
        "top_path": top_path,
    }
    REPORT_PATH.write_text(json.dumps(report) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
