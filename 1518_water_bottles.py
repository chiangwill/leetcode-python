def numWaterBottles(numBottles: int, numExchange: int) -> int:

    ans = 0
    remain = 0

    while numBottles > 0:

        can_drink = (numBottles + remain) // numExchange
        remain = (numBottles + remain) % numExchange

        ans += numBottles

        numBottles = can_drink

    return ans


print(numWaterBottles(9, 3))
print(numWaterBottles(15, 4))
