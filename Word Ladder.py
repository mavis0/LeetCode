from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        #从endWord开始往上找，每次找变化为1的单词记录长度，TLE
        # def distance(w1, w2):
        #     count = 0
        #     for i in range(len(w1)):
        #         if w1[i] != w2[i]:count += 1
        #     return count
        # def getDistance(dp, wordDes, wordVisit, level):
        #     if (not wordDes) or sum(wordVisit) == len(wordList): return
        #     tmp = list()
        #     for word in wordDes:
        #         for i in range(len(wordList)):
        #             if wordVisit[i]:continue
        #             if distance(word, wordList[i]) == 1:
        #                 tmp.append(wordList[i])
        #                 dp[i], wordVisit[i] = level, 1
        #     getDistance(dp, tmp, wordVisit, level+1)
        # dp, res, wordVisit = [-1] * len(wordList), 9999, [0] * len(wordList)
        # if endWord not in wordList: return 0
        # ind = wordList.index(endWord)
        # wordVisit[ind], dp[ind] = 1, 1
        # getDistance(dp, [endWord], wordVisit, 2)
        # for i in range(len(wordList)):
        #     dis = distance(wordList[i], beginWord)
        #     if dis <= 1 and dp[i] != -1:
        #         res = min(dp[i] + dis, res)
        # return res
        #using BFS
        q, res = deque([beginWord]), 1
        if beginWord in wordList: wordList.remove(beginWord)
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord: return res
                for j in range(len(word)):
                    for k in 'abcdefghijklmnopqrstuvwxyz':
                        tmp = word[:j] + k + word[j + 1:]
                        if tmp in wordList and tmp != word:
                            q.append(tmp)
                            wordList.remove(tmp)
            res += 1
        return 0

# print(Solution().ladderLength('a', 'c', [
#     'a', 'b', 'c'
# ]))
print(Solution().ladderLength('hit', 'cog', [
    'hot', 'dot', 'dog', 'lot', 'log', 'cog'
]))
# print(Solution().ladderLength('hot', 'dog', [
#     'hot', 'dog'
# ]))
# print(Solution().ladderLength('cat', 'fin', [
#     "ion","rev","che","ind","lie","wis","oct","ham","jag","ray","nun","ref","wig","jul","ken","mit","eel","paw","per","ola","pat","old","maj","ell","irk","ivy","beg","fan","rap","sun","yak","sat","fit","tom","fin","bug","can","hes","col","pep","tug","ump","arc","fee","lee","ohs","eli","nay","raw","lot","mat","egg","cat","pol","fat","joe","pis","dot","jaw","hat","roe","ada","mac"
# ]))