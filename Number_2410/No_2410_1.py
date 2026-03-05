from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        players.sort()
        trainers.sort()

        index_p, index_t = 0, 0
        res = 0
        while index_p < len(players) and index_t < len(trainers):
            if players[index_p] <= trainers[index_t]:
                res += 1
                index_p += 1
                index_t += 1
            else:
                index_t += 1
        return res

if __name__ == '__main__':
    pass