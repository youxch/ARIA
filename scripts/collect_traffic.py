#!/usr/bin/env python3
"""
Collect GitHub traffic stats and append to traffic/stats.json
Runs daily via GitHub Actions to build a permanent history.
"""

import json
import os
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

TOKEN = os.environ["GH_TOKEN"]
REPO  = os.environ["GH_REPO"]   # e.g. "youxch/ARIA"
OUT   = Path(__file__).parent.parent / "traffic" / "stats.json"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}


def gh_get(path: str) -> dict:
    url = f"https://api.github.com/repos/{REPO}{path}"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


def main():
    OUT.parent.mkdir(exist_ok=True)

    # Load existing accumulated data
    if OUT.exists():
        with open(OUT, encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {
            "repo": REPO,
            "created": datetime.now(timezone.utc).isoformat(),
            "daily_views":  [],   # [{date, count, uniques}]
            "daily_clones": [],
            "snapshots":    [],   # [{timestamp, stars, forks, watchers}]
        }

    # Fetch views (last 14 days)
    views_resp  = gh_get("/traffic/views")
    clones_resp = gh_get("/traffic/clones")

    # Merge new daily views (avoid duplicates by date)
    existing_view_dates = {d["date"] for d in data["daily_views"]}
    for item in views_resp.get("views", []):
        day = item["timestamp"][:10]
        if day not in existing_view_dates:
            data["daily_views"].append({
                "date":    day,
                "count":   item["count"],
                "uniques": item["uniques"],
            })
            existing_view_dates.add(day)

    # Merge new daily clones
    existing_clone_dates = {d["date"] for d in data["daily_clones"]}
    for item in clones_resp.get("clones", []):
        day = item["timestamp"][:10]
        if day not in existing_clone_dates:
            data["daily_clones"].append({
                "date":    day,
                "count":   item["count"],
                "uniques": item["uniques"],
            })
            existing_clone_dates.add(day)

    # Fetch repo metadata snapshot (stars, forks, watchers)
    repo_info = gh_get("")
    data["snapshots"].append({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "stars":     repo_info.get("stargazers_count", 0),
        "forks":     repo_info.get("forks_count", 0),
        "watchers":  repo_info.get("subscribers_count", 0),
        "open_issues": repo_info.get("open_issues_count", 0),
    })

    # Sort by date
    data["daily_views"]  = sorted(data["daily_views"],  key=lambda x: x["date"])
    data["daily_clones"] = sorted(data["daily_clones"], key=lambda x: x["date"])

    # Compute totals
    data["total_views"]   = sum(d["count"]   for d in data["daily_views"])
    data["total_uniques"] = sum(d["uniques"] for d in data["daily_views"])
    data["total_clones"]  = sum(d["count"]   for d in data["daily_clones"])
    data["last_updated"]  = datetime.now(timezone.utc).isoformat()

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"[ARIA Traffic] Updated: "
          f"{data['total_views']} views / "
          f"{data['total_uniques']} unique visitors / "
          f"{data['total_clones']} clones")
    print(f"Stars: {data['snapshots'][-1]['stars']}  "
          f"Forks: {data['snapshots'][-1]['forks']}")


if __name__ == "__main__":
    main()
