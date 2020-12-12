# -- coding: utf-8 --
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # b_more_money_list = list()
        # for i in range(len(costs)):
        #     b_more_money = costs[i][1] - costs[i][0]
        #     b_more_money_list.append({"key": i, "val": b_more_money})
        # b_more_money_list = sorted(b_more_money_list, key=lambda x: x['val'])
        # total = 0
        # for j in range(len(b_more_money_list)):
        #     if j < len(b_more_money_list) / 2:
        #         total += costs[b_more_money_list[j]["key"]][1]
        #     else:
        #         total += costs[b_more_money_list[j]["key"]][0]
        # return total

        costs.sort(key=lambda x: x[0] - x[1])

        total = 0
        for i in range(len(costs)):
            total += costs[i][0] if i < len(costs) / 2 else costs[i][1]
        return total


if __name__ == '__main__':
    s = Solution()
    result = s.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]])
    print result
