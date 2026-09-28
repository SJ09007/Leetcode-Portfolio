class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')
        # Land -> Water
        for i in range(len(landStartTime)):
            landFinish = landStartTime[i] + landDuration[i]
            for j in range(len(waterStartTime)):
                waterFinish = max(landFinish, waterStartTime[j]) + waterDuration[j]
                ans = min(ans, waterFinish)
        # Water -> Land
        for i in range(len(waterStartTime)):
            waterFinish = waterStartTime[i] + waterDuration[i]
            for j in range(len(landStartTime)):
                landFinish = max(waterFinish, landStartTime[j]) + landDuration[j]
                ans = min(ans, landFinish)
        return ans 