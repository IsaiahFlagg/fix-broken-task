Analyze the Apache-style access log at `/app/access.log` and write the result as JSON to `/app/report.json`.

Success criteria:

1. `/app/report.json` exists and contains valid JSON.
2. The JSON value is an object containing exactly these keys: `total_requests`, `unique_ips`, and `top_path`.
3. `total_requests` is an integer equal to the number of non-empty entries in `/app/access.log`.
4. `unique_ips` is an integer equal to the number of distinct client IP addresses in `/app/access.log`.
5. `top_path` is a string equal to the request path that occurs most often in `/app/access.log`.
