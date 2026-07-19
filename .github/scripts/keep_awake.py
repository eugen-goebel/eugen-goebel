"""Visit the deployed Streamlit demos so they do not go to sleep.

Streamlit Community Cloud only counts real browser sessions as activity.
A plain HTTP GET returns the static HTML shell (status 200) without ever
starting the app, so this script uses a headless browser instead and
clicks the wake-up button if an app has already fallen asleep.

Runs from the keep-demos-awake workflow. Local run:
    pip install playwright && playwright install chromium
    python .github/scripts/keep_awake.py
"""

import sys

from playwright.sync_api import sync_playwright

APPS = {
    "etl-pipeline": "https://eugen-goebel-etl-pipeline-app-4shwqu.streamlit.app/",
    "smart-doc-qa": "https://eugen-goebel-smart-doc-qa-app-av3twb.streamlit.app/",
    "predictive-analytics-agent": (
        "https://eugen-goebel-predictive-analytics-agent-app-l05zcc.streamlit.app/"
    ),
    "portfolio-risk-analytics": (
        "https://eugen-goebel-portfolio-risk-analytics.streamlit.app/"
    ),
    "network-threat-analyzer": (
        "https://eugen-goebel-network-threat-analyzer.streamlit.app/"
    ),
}

WAKE_BUTTON_TEXT = "get this app back up"


def visit(page, name: str, url: str) -> bool:
    """Open one app, wake it if needed, and keep the session open briefly."""
    page.goto(url, wait_until="domcontentloaded", timeout=60_000)
    page.wait_for_timeout(8_000)

    wake_button = page.get_by_text(WAKE_BUTTON_TEXT, exact=False)
    if wake_button.count() > 0:
        wake_button.first.click()
        # Cold starts rebuild the app container, give it time to come up
        page.wait_for_timeout(60_000)
        status = "was asleep, woke it up"
    else:
        # Keep the websocket session open long enough to count as a visit
        page.wait_for_timeout(10_000)
        status = "already awake"

    still_asleep = page.get_by_text(WAKE_BUTTON_TEXT, exact=False).count() > 0
    print(f"{name}: {status}" + (" (still waking)" if still_asleep else ""))
    return not still_asleep


def main() -> int:
    failures = 0
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        for name, url in APPS.items():
            try:
                if not visit(page, name, url):
                    failures += 1
            except Exception as exc:  # noqa: BLE001 - report and keep pinging the rest
                print(f"{name}: ERROR {exc}")
                failures += 1
        browser.close()
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
