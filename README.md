# Overview of the Analysis
The purpose of this analysis is to determine if Amazon reviews incentivized by the Vine program are biased towards higher star-ratings. This analysis specifically focuses on reviews made for products in the video game category. The analysis was performed on a subselection of the initial dataset to only include reviews that received 20 or more votes of which at least 50% were considered helpful.

# Results

* There were 40,565 reviews in total in this dataset. The majority of reviews (40,471, 99.77%) came from non-Vine members, while only 94 (0.23%) of the reviews were made by Amazon Vine members.

* There were 15,771 5-star reviews in total in this dataset. The majority of 5-star reviews (15,663, 99.69%) came from non-Vine members, while only 48 (0.31%) of 5-star reviews were made by Amazon Vine members

* Vine reviewers gave a 5-star rating 51.06% of the time, while 38.70% of non-Vine members gave a 5-star rating. 

# Summary

The results of this analysis does suggest that there is positivity bias in Vine reviews. There is a disproportionate number of 5-star reviews (0.31%) made by Vine members who only compose 0.23% of reviewers -- representing a 35% increase over the expected value if there were no difference between the Vine and non-Vine groups. This is also evident by the fact that Vine members gave a 5-star rating 51% of the time, while non-Vine member only gave the same review 39% of the time.

It is also interesting to investigate the mean star-rating of each group -- 4.07 for Vine-members, 4.06 for non-Vine members. While the difference in average rating is only 0.1 stars, even small increases can have a measurable effect on buying patterns of consumers (https://www.nytimes.com/wirecutter/blog/amazon-vine-reviews/). Additionally, the statistical significance of these results can be determined by a Welch's t-test, which accounts for the unequal sample sizes between groups. 