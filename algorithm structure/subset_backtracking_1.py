def find_subsets(start, current_subset, current_sum):
    # 현재 부분집합의 합이 target_sum과 일치하면 result에 추가
    if current_sum == target_sum:
        result.append(current_subset[:])
        return

    # 현재 부분집합의 합이 target_sum을 초과하면 백트래킹
    # 백트래킹을 하지 않았을 때는 지수 시간복잡도를 갖는다.
    if current_sum > target_sum:
        return

    # start부터 nums의 끝까지 탐색
    for i in range(start, len(nums)):
        num = nums[i]
        # 현재 수를 선택한 경우
        current_subset.append(num)
        find_subsets(i + 1, current_subset, current_sum + num)
        print(current_subset)
        # 현재 수를 제외하고, 다른 수를 선택한 경우
        current_subset.pop()


nums = [1, 2, 3, 4, 5]
target_sum = 10
result = []

find_subsets(start=0, current_subset=[], current_sum=0)

print(result)