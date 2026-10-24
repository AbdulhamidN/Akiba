class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losses = {}

        for winner, loser in matches:
            if winner not in losses:
                losses[winner] = 0

            if loser not in losses:
                losses[loser] = 0

            losses[loser] += 1

        no_losses = []
        one_loss = []

        for player in losses:
            if losses[player] == 0:
                no_losses.append(player)
            elif losses[player] == 1:
                one_loss.append(player)

        no_losses.sort()
        one_loss.sort()

        return [no_losses, one_loss]
