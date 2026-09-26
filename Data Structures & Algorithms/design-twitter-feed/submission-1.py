class Twitter:

    def __init__(self):
        self.post = defaultdict(list) # (time, tweetId)
        self.followMap = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.post[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        pq = []

        # retreive tweetIds of user itself  
        if userId in self.post:
            for p in self.post[userId]:
                heapq.heappush(pq, p)        

        # retreive followees of user itself      
        for followed in self.followMap[userId]:
            if followed in self.post:
                for p in self.post[followed]:
                    heapq.heappush(pq, p)

        while len(pq) > 10:
            heapq.heappop(pq)
        #max_heap
        max_heap = [(-time, tweetId) for (time, tweetId) in pq]
        heapq.heapify(max_heap)

        #output
        output = []
        while max_heap:
            output.append(heapq.heappop(max_heap)[1])

        return output    

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
        
