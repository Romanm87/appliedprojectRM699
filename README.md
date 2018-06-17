# appliedprojectRM699

## Abstract

In recent years, Twitter has become a popular microblogging tool for millions of users worldwide. The sum of posted tweets represents a large data source for shared information and opinions regarding a wide range of topics. Academic publications have shown that retrieval of sentiment from tweets related to such topics offers valuable insight in popular opinions that can be used to make predictions. I retrieved a total of 1,020,448 tweets related to six different cryptocurrencies, Cardano, EOS, Ethereum, Litecoin, Ripple, and Stellar to use an artificial neural network to determine the sentiment of their content and to subsequently find correlations among tweet volume, sentiment, and price fluctuations in these cryptocurrencies. With this analysis I found evidence for a strong correlation of sentiment and price among the six cryptocurrencies. However, significant correlation and causative relationships between volume and price and between sentiment and price could only be found in some cases. While discussing the results and their relevance, I also provide ideas for future direction of this study that might strengthen the hypothesis of Twitter data’s predictive power for cryptocurrency price movements. 


## File descriptions (Project branch)

# Python files
train8: train neural network with prelabeled training data 
eval10_test: test results of trained neural network with prelabeled test set
twitter10: retrieve tweets
twitter_cleaning_v10: clean retrieved tweets
eval_run2: function that predicts sentiment of cleaned twitter data when called
eval7_prepare: calls eval_run2 to predict sentiment in tweets

# R files
sentiment_xxx: Plot sentiment, volume, price and find correlations and causative relationships
corr_analysis: find correlations among sentiment and price for each cryptocurrency
sent_distr: Bar plot of the number of negative, neutral, and positive tweets across all cryptocurrencies

