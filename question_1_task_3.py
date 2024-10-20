reviews = ["This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]

def review_summaries(reviews):
    summaries = []
    for review in reviews:
        if len(review) <= 30:
            summaries.append(review)
        else:
            cut_off_index = review.rfind(' ', 0, 30)
            if cut_off_index == -1:
                cut_off_index = 30
            summaries.append(review[:cut_off_index] + "...")
    return summaries
summaries = review_summaries(reviews)
for summary in summaries:
    print(summary)
