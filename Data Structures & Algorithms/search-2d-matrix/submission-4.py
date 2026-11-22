class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s_m = len(matrix)
        l_m = 0
        l = 0
        r_m = s_m
        s = len(matrix[0])
        r = s
        while l_m < r_m:
            i_m = int((l_m + r_m) / 2)
            if target >= matrix[i_m][0] and target <= matrix[i_m][r-1]:
                while l < r:
                    i = int((l + r) / 2)
                    if matrix[i_m][i] == target:
                        return True
                    elif matrix[i_m][i] > target:
                        r = i
                    else:
                        l = i + 1
                return False
            elif target < matrix[i_m][0]:
                r_m = i_m
            else:
                l_m = i_m + 1
        return False


        