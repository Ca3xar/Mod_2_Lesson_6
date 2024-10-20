reviews = ["This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]
keywords = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing", "bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar", "extraordinary"]

def highlight_keywords(reviews, keywords):
    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
            review = review.replace(keyword.capitalize(), keyword.upper())
        print(review)


highlight_keywords(reviews, keywords)