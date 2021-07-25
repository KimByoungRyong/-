def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = list()
    stack.append((0, prices[0]))

    for index in range(1, len(prices)):
        while stack and stack[-1][1] > prices[index]:
            (prev, value) = stack.pop()
            answer[prev] = (index - prev)
        stack.append((index, prices[index]))

    for i in range(len(answer)):
        if answer[i] == 0:
            answer[i] = len(prices) - i - 1
    return answer