import praw
import openai
import os

# Initialize Reddit API
reddit = praw.Reddit(
    client_id="YOUR_REDDIT_CLIENT_ID",
    client_secret="YOUR_REDDIT_CLIENT_SECRET",
    user_agent="YOUR_USER_AGENT",
)

# Initialize OpenAI API
openai.api_key = "YOUR_OPENAI_API_KEY"

# Scrape hot posts from the subreddit
def scrape_hot_posts(subreddit_name, num_posts):
    hot_posts = []
    subreddit = reddit.subreddit(subreddit_name)
    for post in subreddit.hot(limit=num_posts):
        hot_posts.append(post.title)
    return hot_posts

# Generate article using GPT API
def generate_article(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Main function to automate scraping and article generation
def automate_scraping_and_generation(subreddit_name, num_posts):
    hot_posts = scrape_hot_posts(subreddit_name, num_posts)

    for post in hot_posts:
        prompt = f"Write an informative article about the following topic: {post}"
        article = generate_article(prompt)
        print(f"Generated article for topic: {post}\n")
        print(article)
        print("\n" + "=" * 100 + "\n")

# Example usage:
automate_scraping_and_generation("ApplyingToCollege", 5)
