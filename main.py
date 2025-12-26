if __name__ == "__main__":
    print("\n Pulsegen Agentic Review Trend System\n")

    app_id = input("Enter Google Play App ID (e.g. in.swiggy.android): ")
    target_date = input("Enter target date (YYYY-MM-DD): ")

    trend_df = run_monthly_pipeline(app_id, target_date)

    print("\n MONTHLY TREND REPORT\n")
    print(trend_df)

    output_file = f"trend_report_{target_date}.csv"
    trend_df.to_csv(output_file)

    print(f"\n✅ Report saved as {output_file}")
