def run_monthly_pipeline(app_id, target_date):
    target = datetime.strptime(target_date, "%Y-%m-%d")
    month_start = target.replace(day=1)

    dates = []
    d = month_start
    while d <= target:
        dates.append(d.strftime("%Y-%m-%d"))
        d += timedelta(days=1)

    topic_store = defaultdict(lambda: defaultdict(int))

    for date in dates:
        print(f"Processing batch for {date}...")
        process_day(app_id, date, topic_store)

    df = pd.DataFrame(topic_store).fillna(0).astype(int).T
    df = df[dates]

    return df
