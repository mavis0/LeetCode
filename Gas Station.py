class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        #TLE
        # margin, truck, flag = [gas[i]-cost[i] for i in range(len(gas))], 0, False
        # for i in range(len(gas)):
        #     for j in range(i, i+len(gas)):
        #         truck += margin[j % len(gas)]
        #         if truck < 0: break
        #     if j - i + 1 == len(gas) and truck >= 0:
        #         flag = True
        #         break
        #     truck = 0
        # return i if flag else -1
        margin, sum, total, start = [gas[i]-cost[i] for i in range(len(gas))], 0
        for i in range(len(gas)):
            total += margin[i]
            sum += margin[i]
            if sum < 0:
                start, sum = i + 1, 0
        return -1 if total < 0 else start

print(Solution().canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))