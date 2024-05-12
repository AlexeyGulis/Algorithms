from typing import List


class Twitter:
    user_twit = None
    twit_user = None
    twits = None
    followers = None

    def __init__(self):
        self.user_twit = {}
        self.twit_user = {}
        self.twits = []
        self.followers = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.user_twit:
            self.user_twit[userId].append(tweetId)
        else:
            self.user_twit[userId] = [tweetId]
        self.twit_user[tweetId] = userId
        self.twits.append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        j = 0
        twit_news = []
        for i in range(len(self.twits) - 1, -1, -1):
            if j == 10:
                break
            if self.twit_user[self.twits[i]] == userId:
                twit_news.append(self.twits[i])
                j += 1
            else:
                if userId in self.followers:
                    if self.twit_user[self.twits[i]] in self.followers[userId]:
                        twit_news.append(self.twits[i])
                        j += 1
        return twit_news

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            if followeeId not in self.followers[followerId]:
                self.followers[followerId].append(followeeId)
        else:
            self.followers[followerId] = [followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            if followeeId in self.followers[followerId]:
                del self.followers[followerId][self.followers[followerId].index(followeeId)]


# Your Twitter object will be instantiated and called as such:
def help_funct(list1,list2):
    answer = []
    obj = None
    for i in range(len(list1)):
        if list1[i] == 'Twitter':
            obj = Twitter()
            answer.append(None)
        if list1[i] == 'postTweet':
            answer.append(obj.postTweet(list2[i][0],list2[i][1]))
        if list1[i] == 'getNewsFeed':
            answer.append(obj.getNewsFeed(list2[i][0]))
        if list1[i] == 'follow':
            answer.append(obj.follow(list2[i][0], list2[i][1]))
        if list1[i] == 'unfollow':
            answer.append(obj.unfollow(list2[i][0], list2[i][1]))

    return answer

print(help_funct(["Twitter","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet",
                  "postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet",
                  "postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed",
                  "follow","getNewsFeed","unfollow","getNewsFeed"],[[],[1,5],[2,3],[1,101],[2,13],[2,10],[1,2],[1,94],[2,505],[1,333],[2,22],[1,11],[1,205],[2,203],[1,201],[2,213],[1,200],
                                                                    [2,202],[1,204],[2,208],[2,233],[1,222],[2,211],[1],[1,2],[1],[1,2],[1]]))
