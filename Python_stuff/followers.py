# This program gives the followers list of an inputted user plus some extra stats about them, such as the average number of followers of someone following them.

import requests
import json
import os
import time


def clear():
    os.system('clear')


clear()

done = False
offset = 0
page = 1
followers = []
username = input("Which user? \n")
username = str.lower(username)
while done == False:
    print(f"Obtaining page {page}... (currently {len(followers)})")
    with requests.get(
            f"https://api.scratch.mit.edu/users/{username}/followers?offset={offset}"
    ) as request:
        followers.extend(request.json())
        if (len(request.json()) != 20):
            done = True
        else:
            offset += 20
            page += 1
print(f"Done! Final count is {len(followers)}.")
time.sleep(0.3)
print('Clearing console')
time.sleep(0.7)
clear()

most_followers = 0
most_followed_user = ''
total_followers = 0
errors = 0
spaces = " " * 25
print("\n" + ("-" * 45))
print(f"User {spaces} Followers")
print("-" * 45)
for follower in followers:
    user_follows = requests.get(
        f'https://scratchdb.lefty.one/v2/user/info/{follower["username"]}'
    ).text
    user_follows = json.loads(user_follows)
    spaces = 25 - len(follower["username"])
    spaces = " " * spaces
    if "followers" in user_follows:
        user_follows = user_follows["followers"]
        print(
            follower["username"],
            end=f", {spaces}|   {user_follows} followers" + "\n")
        total_followers += user_follows
        if user_follows >= most_followers:
            most_followed_user = follower["username"]
            most_followers = user_follows
    else:
        print(f"{follower['username']}  {spaces}|   [Deleted user]")
        errors += 1

print(
    f"\n\nUser stats for {str.title(username)}:\n\tFollowers of their followers: {total_followers}\n\tDeleted users following them: {errors}\n\tMost followed user:{most_followed_user} ({most_followers} followers)\n\tAverage followers of their followers: {round(total_followers/len(followers))}"
)