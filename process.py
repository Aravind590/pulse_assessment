def process_day(app_id, date, store):
    reviews = fetch_reviews_for_date(app_id, date)

    for review in reviews:
        topic = agentic_topic_extractor(review)
        store[topic][date] += 1
