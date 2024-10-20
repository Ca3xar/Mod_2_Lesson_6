reviews = ["This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]


def keyword_tally(reviews):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing", "extraordinary"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar",]

    positive_count = 0
    negative_count = 0
    
    for review in reviews:
        words = review.lower().split()
        for word in words:
            if word in positive_words:
                positive_count += 1
            elif word in negative_words:
                negative_count += 1
    return positive_count, negative_count


positive_count, negative_count = keyword_tally(reviews)
print(f"positive words count: {positive_count}")
print(F"negative words count: {negative_count}")

#can I get some feedback on this to why its incorrectly counting the keywords