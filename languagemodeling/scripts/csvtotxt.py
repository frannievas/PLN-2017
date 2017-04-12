import csv

csv_head = ('timestamp_ms,id,user,following,follower,location,time_zone,'
            'tweet_id,is_retweet,mentions_id,'
            'mentions_username,hashtags,tweet\n')

# Open output csv file
csva = open('ouput.txt', 'a')

with open('tweets_24M.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        # print(row)
        # print("\n")
        # for timestamp_ms,id,user,following,follower,location,time_zone,
        # tweet_id,is_retweet,mentions_id,mentions_username,hashtags,tweet,
        #  tweets_count in row:
        # for i in range(len(row)):
            # print(row[12])
        csva.write(row[12] + "\n")
