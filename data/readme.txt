Data is 20090 short stories from the "ShortScaryStories" subreddit.
You can obtain them from my Google cloud file system. 

Spanning time: 
14th Feb 2018 to 18th Jan 2013
1487048400 to 1358485200

Data:
1. dataCleaned: This is reddit data with only those fields that are important for our analyses.
2. dataWithComments: All data in the subreddit with first level of comments.

Properties of the file:
- A list of dictionaries containing properties of the "Submission" object. Can be loaded as a JSON object.
- Contains details like: title, post content, author name, upvotes etc.
- The submissions are not in order of time. This shouldn't matter much.
- Does not contain comments.

Relevant fields:
subreddit_id
selftext
id
author
score
num_comments
name
created
title
comments
author_flair_text

Relevant comment fields:
id
author
parent_id
score
body
is_submitter
name
created
controversiality
