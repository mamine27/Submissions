# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/


class TN:
    def __init__(self):
        self.org = 0
        self.all = 0
        self.children = defaultdict(int)

class MapSum:

    def __init__(self):
        self.root = TN()
        

    def insert(self, key: str, val: int) -> None:

        def ins(indx = 0 , cur = self.root , val = val):
            
            if indx == len(key):
                dlt = val - cur.org
                cur.all += dlt
                cur.org = val 
                return dlt
            if key[indx]  not in cur.children:
                cur.children[key[indx]] = TN()

            vl = ins(indx + 1 , cur.children[key[indx]])
            cur.all += vl
            return vl
        ins()
        # print("here",ins())
            



        

    def sum(self, prefix: str) -> int:
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return 0
            cur = cur.children[ch]
            # print(cur.all , "h------")/

        return cur.all
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)