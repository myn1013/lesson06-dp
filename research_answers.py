# -*- coding: utf-8 -*-
"""
独立研究任务答案
1. 回溯法 n= 后是什么（8 分）
2. 完全背包改哪行（7 分）
3. 分支限界一句话（5 分）
"""


def research_1_backtracking_terminal():
    """
    研究任务 1：回溯法中 n= 后是什么？

    答：在背包回溯法中，递归函数通常写作 backtrack(i, cw, cv)，
    i 表示「正在考虑第 i 个物品」，n 是物品总数。
    当 i == n 时，说明所有物品都已决策完毕（每个物品都已决定选或不选），
    到达了搜索树的叶子节点。此时应当用当前累计价值 cv 更新全局最优解 best，
    然后 return（回溯）。

    也就是说，i == n 是递归的**终止条件（边界）**：
      - 动作：if cv > best: best = cv
      - 然后：return

    伪代码：
        def backtrack(i, cw, cv):
            if i == n:               # n 个物品全部考虑完
                if cv > best:        # 更新最优解
                    best = cv
                return               # 回溯到上一层
            # 选第 i 个物品
            if cw + w[i] <= capacity:
                backtrack(i + 1, cw + w[i], cv + v[i])
            # 不选第 i 个物品
            backtrack(i + 1, cw, cv)
    """
    print("【研究任务 1】回溯法 n= 后是什么？")
    print("  当 i == n（物品全部考虑完毕）时，到达递归边界：")
    print("    1) 用当前累计价值 cv 更新全局最优 best；")
    print("    2) return，回溯到上一层继续搜索。")
    print("  即 i==n 是叶子节点 → 更新最优解 → 返回。")


def research_2_complete_knapsack_change():
    """
    研究任务 2：完全背包改哪行？

    答：0/1 背包与完全背包的唯一区别是内层容量循环的方向。

    0/1 背包（每个物品最多用 1 次）——内层**逆序**：
        for i in range(n):
            for j in range(capacity, w[i] - 1, -1):   # ← 逆序
                dp[j] = max(dp[j], dp[j - w[i]] + v[i])

    完全背包（每个物品可用无限次）——把内层改为**正序**：
        for i in range(n):
            for j in range(w[i], capacity + 1):        # ← 正序（只改这一行）
                dp[j] = max(dp[j], dp[j - w[i]] + v[i])

    原理：0/1 背包逆序是为了保证 dp[j - w[i]] 取的是「上一层（未放 i）」的值，
    避免同一物品被重复使用；完全背包正序则允许 dp[j - w[i]] 已经包含了物品 i，
    从而实现同一物品多次选取。
    """
    print("\n【研究任务 2】完全背包改哪行？")
    print("  只需把内层容量循环由「逆序」改为「正序」：")
    print("  0/1 背包:  for j in range(capacity, w[i]-1, -1):")
    print("  完全背包:  for j in range(w[i], capacity+1):")
    print("  （其余行不变。正序使得同一物品可被多次取用。）")


def research_3_branch_and_bound():
    """
    研究任务 3：分支限界一句话。

    答：分支限界是一种在状态空间树上按「限界函数」估算每个节点
    所能达到的最优上界，若该上界不优于当前已知最优解则剪枝（不再扩展该分支），
    从而大幅减少搜索量的最优化搜索算法。
    """
    print("\n【研究任务 3】分支限界一句话？")
    print("  分支限界：按限界函数估算每个节点的最优上界，")
    print("  若上界不优于当前最优解则剪枝，从而高效缩小搜索空间的搜索算法。")


if __name__ == "__main__":
    research_1_backtracking_terminal()
    research_2_complete_knapsack_change()
    research_3_branch_and_bound()
