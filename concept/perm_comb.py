# 원소들이 중복이 없다고 가정한다
items = [1, 2, 3, 4, 5, 6, 7]


def combination(items, k):
    """items에서 순서상관없이 k개를 뽑는 모든 경우를 반환하는 함수

    :param items:
        중복되지 않는 원소들이 담긴 리스트(배열)
    :param k:
        중복되지 않게 뽑을 원소의 수(int)
    """
    ans = []
    n = len(items)

    # 핵심 재귀함수 (dfs)
    def _dfs(start, comb):
        nonlocal ans, items, n, k
        if len(comb) == k:
            ans += [comb]
            return

        remain = k - len(comb)
        for i in range(start, n - remain + 1):
            _dfs(i + 1, comb + [items[i]])

    _dfs(0, [])
    return ans


ans = combination(items, 3)
print(f"combination ({len(ans)})")
print(ans)


def permutation(items, k):
    """items의 원소에서 순서를 고려하여 k개를 뽑는 모든 집합을 반환하는 함수"""
    ans = []
    n = len(items)
    used = [False for _ in range(n)]

    # 핵심 재귀함수 (DFS)
    def _core(per):
        nonlocal ans, n, k, used
        if len(per) == k:
            ans += [per]
            return

        for i in range(n):
            if not used[i]:
                used[i] = True
                _core(per + [items[i]])
                used[i] = False

    _core([])
    return ans


ans = permutation(items, 3)
print(f"permutation ({len(ans)})")
print(ans)

# combination을 전부구하는 새로운 방법
# ------------------------------------
nums = [1, 2, 3, 4, 5]
answer_list = []


def combi(n, ans):
    if n == len(nums):
        temp = [i for i in ans]
        answer_list.append(temp)
        return
    ans.append(nums[n])
    combi(n + 1, ans)
    ans.pop()
    combi(n + 1, ans)


combi(0, [])
print(answer_list)
