import praw

# authenticate to Reddit API
reddit = praw.Reddit(client_id='EskwcO6JSqqeGHCFgdhSuw',
                     client_secret='hlP3FHqbqnmGj0kasYj7l71kQwfyNQ',
                     user_agent='final')

# specify the subreddit and thread ID
subreddit = reddit.subreddit('spotify')
thread_id = 'wc7sjj'

# get the submission object for the thread
submission = reddit.submission(id=thread_id)

# flatten comment tree and sort by score (highest first)
submission.comment_sort = 'top'
submission.comments.replace_more(limit=10)
comments = submission.comments.list()
comments = sorted(comments, key=lambda x: x.score, reverse=True)

# write comments and up/downvote info to file
with open('spotify_comments.txt', 'a') as f:
    for i, comment in enumerate(comments):
        f.write(f'Comment {i+1}:\n')
        f.write(f'Text: {comment.body}\n')
        f.write(f'Upvotes: {comment.score}\n')
        f.write(f'Downvotes: {comment.downs}\n')
        f.write(f'Total awards: {comment.total_awards_received}\n\n')

print("done")
