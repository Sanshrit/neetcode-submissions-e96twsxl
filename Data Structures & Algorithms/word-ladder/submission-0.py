class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        m = "abcdefghijklmnopqrstuvwxyz"
        words = set()
        for word in wordList:
            words.add(word)
        

        if beginWord in words:
            words.remove(beginWord)
        if endWord not in words:
            return 0
        q.append([beginWord,1])
        while q:
            currWord,currLen = q.popleft()
            for idx in range(len(currWord)):
                temp = list(currWord)
                for i in range(len(m)):
                    temp[idx] = m[i]
                    st = "".join(temp)
                    if st == endWord:
                        return currLen+1
                    if st in words:
                        q.append([st,currLen+1])
                        words.remove(st)
        return 0
            

        