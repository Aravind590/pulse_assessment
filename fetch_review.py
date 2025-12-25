
from google_play_scraper import reviews, Sort
from datetime import datetime, timedelta
from collections import defaultdict
import pandas as pd


def fetch_reviews_for_date(app_id, date_str):
    target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    collected = []
    token = None

    while True:
        result, token = reviews(
            app_id,
            lang="en",
            country="in",
            sort=Sort.NEWEST,
            count=200,
            continuation_token=token
        )

        if not result:
            break

        for r in result:
            review_date = r["at"].date()

            if review_date == target_date:
                collected.append(r["content"])

            if review_date < target_date:
                return collected

        if token is None:
            break

    return collected
