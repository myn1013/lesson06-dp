# -*- coding: utf-8 -*-
"""
Step1 凑硬币：贪心 vs 动态规划
检查点：贪心 5 枚 vs 动规 3 枚
硬币面值：[1, 5, 11]，目标金额：15
"""

COINS = [1, 5, 11]
AMOUNT = 15


def greedy_coin_change(coins, amount):
    """贪心算法：每次取最大面值硬币"""
    coins_sorted = sorted(coins, reverse=True)
    result = []
    remaining = amount
    for coin in coins_sorted:
        while remaining >= coin:
            result.append(coin)
            remaining -= coin
    return result


def dp_coin_change(coins, amount):
    """动态规划：求最少硬币数，并回溯出具体组合"""
    INF = float('inf')
    # dp[i] 表示凑出金额 i 所需的最少硬币数
    dp = [INF] * (amount + 1)
    dp[0] = 0
    # prev[i] 记录凑出金额 i 时最后使用的硬币，用于回溯
    prev = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                prev[i] = coin

    if dp[amount] == INF:
        return [], -1

    # 回溯出具体硬币组合
    combination = []
    cur = amount
    while cur > 0:
        coin = prev[cur]
        combination.append(coin)
        cur -= coin
    return combination, dp[amount]


def main():
    print("=" * 60)
    print("Step1 凑硬币问题")
    print(f"硬币面值：{COINS}")
    print(f"目标金额：{AMOUNT}")
    print("=" * 60)

    # 贪心算法
    greedy_result = greedy_coin_change(COINS, AMOUNT)
    print(f"\n【贪心算法】")
    print(f"  硬币组合：{greedy_result}")
    print(f"  硬币数量：{len(greedy_result)} 枚")
    print(f"  金额校验：{sum(greedy_result)} (应为 {AMOUNT})")

    # 动态规划
    dp_combination, dp_count = dp_coin_change(COINS, AMOUNT)
    print(f"\n【动态规划】")
    print(f"  硬币组合：{dp_combination}")
    print(f"  硬币数量：{dp_count} 枚")
    print(f"  金额校验：{sum(dp_combination)} (应为 {AMOUNT})")

    # 对比
    print(f"\n【对比结论】")
    print(f"  贪心：{len(greedy_result)} 枚，动规：{dp_count} 枚")
    if len(greedy_result) > dp_count:
        print(f"  → 贪心并非最优，动规少用了 {len(greedy_result) - dp_count} 枚硬币")

    print("\n" + "=" * 60)
    print("检查点：贪心 5 枚 vs 动规 3 枚")
    assert len(greedy_result) == 5, f"贪心应为 5 枚，实际 {len(greedy_result)} 枚"
    assert dp_count == 3, f"动规应为 3 枚，实际 {dp_count} 枚"
    print("✓ 检查点通过：贪心 5 枚，动规 3 枚")
    print("=" * 60)


if __name__ == "__main__":
    main()
