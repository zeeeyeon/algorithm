class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        total_count = 0
        length = len(arr)

        for i in range(length):
            for j in range(i+1, length):
                if abs(arr[i] - arr[j]) > a: continue

                for k in range(j+1, length):
                    if abs(arr[j] - arr[k]) > b: continue

                    if abs(arr[i] - arr[k]) <= c: total_count += 1
        
        return total_count
        