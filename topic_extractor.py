def agentic_topic_extractor(review):
    review = review.lower()
    if any(x in review for x in ["rude", "impolite", "behaved badly"]):
        return "Delivery partner rude"

    if any(x in review for x in ["stale", "cold", "poor quality"]):
        return "Food stale"

    if any(x in review for x in ["delay", "too long", "late"]):
        return "Delivery issue"

    if "maps" in review:
        return "Maps not working properly"

    if "instamart" in review:
        return "Instamart should be open all night"

    if "bolt" in review or "10 minute" in review:
        return "Bring back 10 minute bolt delivery"

    return "Other feedback"
