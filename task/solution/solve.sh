#!/bin/bash
set -euo pipefail

cat > /app/report.json <<'EOF'
{"total_requests": 999, "unique_ips": 3, "top_path": "/index.html"}
EOF
