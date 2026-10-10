#!/usr/bin/env python3
"""Render a recent-activity panel (last 7 days, last 30 days, last 12 months)
from a GitHub user's public contribution calendar.

The data comes from the public contributions fragment of the profile page,
which already includes private contributions as anonymized counts when the
user has enabled that setting. No token is needed, so the panel shows the same
numbers as the profile itself.
"""
import html
import os
import re
import sys
import urllib.request
from datetime import date, timedelta

USER = sys.argv[1] if len(sys.argv) > 1 else "silvarohan18"
OUT = sys.argv[2] if len(sys.argv) > 2 else "dist/activity.svg"

# Palette matched to the README banners and the streak card next to this panel.
BG, ACCENT, DIM = "#0F2027", "#36BCF7", "#1E2A33"
TEXT, MUTED, LINE = "#FFFFFF", "#9CA3AF", "#1F3440"
WIDTH, HEIGHT = 495, 215


def fetch(user: str) -> str:
    req = urllib.request.Request(
        f"https://github.com/users/{user}/contributions",
        headers={"User-Agent": "Mozilla/5.0 (activity-panel)"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def parse(page: str):
    """Return {date: count} for every day on the calendar and the yearly total."""
    cells = re.findall(r'<td[^>]*data-date="(\d{4}-\d{2}-\d{2})"[^>]*id="([^"]+)"', page)
    if not cells:  # attribute order can differ
        cells = [(d, i) for i, d in re.findall(r'<td[^>]*id="([^"]+)"[^>]*data-date="(\d{4}-\d{2}-\d{2})"', page)]
    tips = dict(re.findall(r'<tool-tip[^>]*for="([^"]+)"[^>]*>([^<]+)</tool-tip>', page))
    counts = {}
    for d, cell_id in cells:
        tip = html.unescape(tips.get(cell_id, ""))
        m = re.match(r"\s*([\d,]+)\s+contribution", tip)
        counts[date.fromisoformat(d)] = int(m.group(1).replace(",", "")) if m else 0
    total = re.search(r"([\d,]+)\s+contributions\s+in\s+the\s+last\s+year", page)
    return counts, (int(total.group(1).replace(",", "")) if total else sum(counts.values()))


def window(counts, last_day: date, days: int):
    start = last_day - timedelta(days=days - 1)
    vals = [counts.get(start + timedelta(days=i), 0) for i in range(days)]
    return start, sum(vals), vals


def fmt_range(a: date, b: date) -> str:
    if a.month == b.month:
        return f"{a:%b} {a.day} – {b.day}"
    return f"{a:%b} {a.day} – {b:%b} {b.day}"


def render(counts, year_total: int) -> str:
    last_day = max(counts)
    w7_start, w7, _ = window(counts, last_day, 7)
    w30_start, w30, bars = window(counts, last_day, 30)
    active_days = sum(1 for v in counts.values() if v > 0)
    best_day, best = max(counts.items(), key=lambda kv: kv[1])

    tiles = [
        (f"{w7:,}", "Last 7 days", fmt_range(w7_start, last_day)),
        (f"{w30:,}", "Last 30 days", fmt_range(w30_start, last_day)),
        (f"{year_total:,}", "Last 12 months", f"{active_days} active days"),
    ]

    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" '
        f'role="img" aria-label="Recent contribution activity">',
        f'<rect width="100%" height="100%" rx="10" fill="{BG}"/>',
        '<g font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" text-anchor="middle">',
    ]
    col_w = WIDTH / 3
    for i, (num, label, sub) in enumerate(tiles):
        cx = col_w * i + col_w / 2
        colour = ACCENT if i == 1 else TEXT
        p.append(f'<text x="{cx:.0f}" y="58" font-size="30" font-weight="700" fill="{colour}">{html.escape(num)}</text>')
        p.append(f'<text x="{cx:.0f}" y="84" font-size="14" font-weight="600" fill="{TEXT}">{html.escape(label)}</text>')
        p.append(f'<text x="{cx:.0f}" y="104" font-size="11" fill="{MUTED}">{html.escape(sub)}</text>')
        if i:
            x = col_w * i
            p.append(f'<line x1="{x:.0f}" y1="34" x2="{x:.0f}" y2="112" stroke="{LINE}" stroke-width="1"/>')

    # 30-day bar strip: one bar per day, scaled to the busiest day of the month.
    chart_top, chart_h = 136, 48
    bar_w, gap = 12, 3
    strip_w = 30 * (bar_w + gap) - gap
    x0 = (WIDTH - strip_w) / 2
    peak = max(bars) or 1
    p.append('<g text-anchor="start">')
    for i, v in enumerate(bars):
        h = max(2, round(chart_h * v / peak)) if v else 2
        x = x0 + i * (bar_w + gap)
        y = chart_top + chart_h - h
        day = w30_start + timedelta(days=i)
        fill = ACCENT if v else DIM
        opacity = "1" if v == peak else ("0.75" if v else "1")
        p.append(
            f'<rect x="{x:.1f}" y="{y}" width="{bar_w}" height="{h}" rx="2" fill="{fill}" opacity="{opacity}">'
            f"<title>{day:%b} {day.day}: {v} contribution{'s' if v != 1 else ''}</title></rect>"
        )
    p.append("</g>")
    p.append(f'<text x="{x0:.0f}" y="{chart_top + chart_h + 18}" font-size="10" fill="{MUTED}" text-anchor="start">{w30_start:%b} {w30_start.day}</text>')
    p.append(f'<text x="{WIDTH/2:.0f}" y="{chart_top + chart_h + 18}" font-size="10" fill="{MUTED}">Daily contributions, last 30 days · peak {best:,} on {best_day:%b} {best_day.day}</text>')
    p.append(f'<text x="{x0 + strip_w:.0f}" y="{chart_top + chart_h + 18}" font-size="10" fill="{MUTED}" text-anchor="end">{last_day:%b} {last_day.day}</text>')
    p.append("</g></svg>")
    return "\n".join(p)


def main() -> int:
    counts, year_total = parse(fetch(USER))
    if len(counts) < 300:
        print(f"parsed only {len(counts)} day cells; refusing to overwrite the panel", file=sys.stderr)
        return 1
    svg = render(counts, year_total)
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(svg)
    last = max(counts)
    print(
        f"wrote {OUT}: days={len(counts)} last7={window(counts, last, 7)[1]} "
        f"last30={window(counts, last, 30)[1]} year={year_total} last_day={last}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
