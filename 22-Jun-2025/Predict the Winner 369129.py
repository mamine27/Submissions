# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        tot = sum(nums)
        score = 0
        # def winner(arr = nums , player = True):
        #     nonlocal score , tot
        #     if  len (arr)== 1:
        #         if player:
        #             score += arr[0]
        #         return score >= tot - score
            
        #     if (len(arr) == 2 and arr[0] > arr[1]) or (max(arr[0] , arr[-2]) > max(arr[1] , arr[-1])):
        #         if player:
        #             score += arr[0]
        #         return winner(arr[1:] , player = not player)
        #     elif (len(arr) ==2 and arr[0] <= arr[1])  or max(arr[0] , arr[-2]) < max(arr[1] , arr[-1]):
        #         if player:
        #             score += arr[-1]
        #         return winner(arr[:-1] ,player = not player)
        #     elif min(arr[0] , arr[-2]) > min(arr[1] , arr[-1]):
        #         if player:
        #             score += arr[0]
        #         return winner(arr[1:] , player = not player)
        #     else:
        #         if player:
        #             score += arr[-1]
        #         return winner(arr[:-1] ,player = not player)



        # print(score)
        def winner(arr = nums , player = True , score = 0):
            if not arr:
                return score >= tot - score
            
            if player and arr:
                return winner(arr[1:] , False , score + arr[0]) or winner(arr[:-1] , False, score + arr[-1])
            elif arr:
                return winner(arr[1:] , True , score ) and winner(arr[:-1] , True , score)
                
        return winner()


        