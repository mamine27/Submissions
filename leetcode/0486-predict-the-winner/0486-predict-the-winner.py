class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        tot = sum(nums)
        # score = 0
        def winner(arr = nums , player = True , score = 0):
            if not arr:
                return score >= tot - score
            
            if player:
                return winner(arr[1:] , False , score + arr[0]) or winner(arr[:-1] , False, score + arr[-1])
            else:
                return winner(arr[1:] , True , score ) and winner(arr[:-1] , True , score)
                
        return winner()