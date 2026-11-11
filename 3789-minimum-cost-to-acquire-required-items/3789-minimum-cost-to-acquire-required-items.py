class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        option1 = (cost1 * need1) + (cost2 * need2)

        option2 = costBoth * max(need1, need2)

        option3 = (costBoth * min(need1, need2) +
                   cost1 * max(0, need1 - need2) +
                   cost2 * max(0, need2 - need1))

        return min(option1, option2, option3)