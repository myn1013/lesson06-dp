# -*- coding: utf-8 -*-
"""
Step2 + Task4 + Task5：0/1 背包问题
检查点：背包最优 315、组合 [3, 4, 5]
附加：预算 800 对比、必投项目约束
"""

# 6 个项目（0 索引），每项有重量（成本）和价值（收益）
WEIGHTS = [50, 45, 40, 15, 25, 35]
VALUES = [40, 50, 60, 95, 105, 115]
CAPACITY = 75          # 基础预算
BUDGET_800 = 800       # Task4：放宽到 800 的对比预算
MANDATORY_ITEM = 0     # Task5：必投项目（项目 0 必须选）


def knapsack_dp(weights, values, capacity, mandatory=None):
    """
    0/1 背包动态规划，返回 (最优价值, 选中物品索引列表)。
    mandatory: 必投物品索引（必须选入背包），None 表示无约束。
    """
    n = len(weights)

    # 处理必投约束：先扣除必投物品的重量和价值
    base_value = 0
    base_weight = 0
    mandatory_set = set()
    if mandatory is not None:
        base_value = values[mandatory]
        base_weight = weights[mandatory]
        mandatory_set.add(mandatory)
        capacity -= base_weight
        if capacity < 0:
            return -1, []  # 必投物品本身就超重，无解

    # dp[j] 表示容量 j 下的最大价值
    dp = [0] * (capacity + 1)
    # 记录决策：choose[i][j] = True 表示在考虑前 i+1 个物品、容量 j 时选了第 i 个物品
    choose = [[False] * (capacity + 1) for _ in range(n)]

    for i in range(n):
        if i in mandatory_set:
            continue  # 必投物品已在 base 中，不再参与 DP
        # 0/1 背包：逆序遍历容量，保证每个物品只用一次
        for j in range(capacity, weights[i] - 1, -1):
            if dp[j - weights[i]] + values[i] > dp[j]:
                dp[j] = dp[j - weights[i]] + values[i]
                choose[i][j] = True

    best_value = dp[capacity] + base_value

    # 回溯出选中的物品组合
    selected = list(mandatory_set)
    j = capacity
    for i in range(n - 1, -1, -1):
        if i in mandatory_set:
            continue
        if choose[i][j]:
            selected.append(i)
            j -= weights[i]
    selected.sort()

    return best_value, selected


def print_items(title, weights, values):
    print(title)
    print(f"{'编号':>4} {'重量':>6} {'价值':>6} {'性价比':>8}")
    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        print(f"{i:>4} {weights[i]:>6} {values[i]:>6} {ratio:>8.2f}")


def main():
    print("=" * 70)
    print("Step2 0/1 背包问题")
    print("=" * 70)
    print_items("项目清单：", WEIGHTS, VALUES)

    # ---------- Step2：基础背包 ----------
    print("\n" + "-" * 70)
    print(f"【Step2】基础背包（预算 = {CAPACITY}）")
    print("-" * 70)
    best_val, selected = knapsack_dp(WEIGHTS, VALUES, CAPACITY)
    total_w = sum(WEIGHTS[i] for i in selected)
    print(f"  最优价值：{best_val}")
    print(f"  选中项目：{selected}")
    print(f"  总重量：{total_w} / {CAPACITY}")
    assert best_val == 315, f"最优价值应为 315，实际 {best_val}"
    assert selected == [3, 4, 5], f"组合应为 [3,4,5]，实际 {selected}"
    print("  ✓ 检查点通过：最优 315，组合 [3, 4, 5]")

    # ---------- Task4：预算 800 对比 ----------
    print("\n" + "-" * 70)
    print(f"【Task4】预算 800 对比（原预算 {CAPACITY} → 新预算 {BUDGET_800}）")
    print("-" * 70)
    best_val_800, selected_800 = knapsack_dp(WEIGHTS, VALUES, BUDGET_800)
    total_w_800 = sum(WEIGHTS[i] for i in selected_800)
    print(f"  预算 {CAPACITY}：最优价值 = {best_val}，组合 = {selected}")
    print(f"  预算 {BUDGET_800}：最优价值 = {best_val_800}，组合 = {selected_800}")
    print(f"  总重量：{total_w_800} / {BUDGET_800}")
    print(f"  价值提升：{best_val_800 - best_val}（{(best_val_800 - best_val) / best_val * 100:.1f}%）")
    if selected_800 == list(range(len(WEIGHTS))):
        print("  → 预算 800 足以买下全部项目，因此取走所有项目。")

    # ---------- Task5：必投项目约束 ----------
    print("\n" + "-" * 70)
    print(f"【Task5】必投项目约束（项目 {MANDATORY_ITEM} 必须选，预算 = {CAPACITY}）")
    print("-" * 70)
    best_val_m, selected_m = knapsack_dp(WEIGHTS, VALUES, CAPACITY, mandatory=MANDATORY_ITEM)
    total_w_m = sum(WEIGHTS[i] for i in selected_m)
    print(f"  必投项目 {MANDATORY_ITEM}：重量 {WEIGHTS[MANDATORY_ITEM]}，价值 {VALUES[MANDATORY_ITEM]}")
    print(f"  最优价值：{best_val_m}")
    print(f"  选中项目：{selected_m}")
    print(f"  总重量：{total_w_m} / {CAPACITY}")
    print(f"  与无约束对比：价值 {best_val} → {best_val_m}（下降 {best_val - best_val_m}）")
    print(f"  → 必投项目性价比最低（{VALUES[MANDATORY_ITEM] / WEIGHTS[MANDATORY_ITEM]:.2f}），"
          f"强制选入后挤占了高性价比项目的预算。")

    print("\n" + "=" * 70)
    print("全部检查点通过 ✓")
    print("=" * 70)


if __name__ == "__main__":
    main()
