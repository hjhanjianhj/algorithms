"""
汉诺塔问题

增加限制：
不能直接从最左边到最右边，也不能直接从最右边到最左边，必须经过中间
"""
import enum
import sys
from enum import Enum

LEFT = 'left'
MID = 'mid'
RIGHT = 'right'

def process(num, _from, _to):
    if num == 1:
        if _from == MID or _to == MID:
            print_step(_from, _to, num)
            return 1
        else:
            print_step(_from, MID, num)
            print_step(MID, _to, num)
            return 2

    if _from == MID or _to == MID:
        other = LEFT if _from == RIGHT or _to == RIGHT else RIGHT
        part1 = process(num - 1, _from, other)
        print_step(_from, _to, num)
        part2 = 1
        part3 = process(num - 1, other, _to)
        return part1 + part2 + part3
    else:
        part1 = process(num - 1, _from, _to)
        print_step(_from, MID, num)
        part2 = 1
        part3 = process(num - 1, _to, _from)
        print_step(MID, _to, num)
        part4 = 1
        part5 = process(num - 1, _from, _to)
        return part1 + part2 + part3 + part4 + part5


def print_step(_from, _to, num):
    print(f'Move {num} from {_from} to {_to}')


def hanoi_by_re(num):
    """
    递归实现汉诺塔
    :return: 
    """
    return process(num, LEFT, RIGHT)

class ActionType(Enum):
    NO_ACTION = 1
    LEFT_TO_MID = 2
    MID_TO_LEFT = 3
    RIGHT_TO_MID = 4
    MID_TO_RIGHT = 5


def process_by_stack(pre_actions, no_action, action, from_stack, to_stack, _from, _to):
    pre_action = pre_actions[0]
    if pre_action != no_action and from_stack[-1] < to_stack[-1]:
        data = from_stack.pop()
        to_stack.append(data)
        pre_actions[0] = action
        print(f"Move {data} from {_from} to {_to}")
        return 1
    return 0


def hanoi_by_stack(num):
    left_stack = []
    mid_stack = []
    right_stack = []
    left_stack.append(sys.maxsize)
    mid_stack.append(sys.maxsize)
    right_stack.append(sys.maxsize)
    for i in range(num, 0, -1):
        left_stack.append(i)
    curr_action = [ActionType.NO_ACTION]
    step_count = 0

    while len(right_stack) < num + 1:
        step_count += process_by_stack(curr_action, ActionType.MID_TO_LEFT, ActionType.LEFT_TO_MID, left_stack, mid_stack, LEFT, MID)
        step_count += process_by_stack(curr_action, ActionType.LEFT_TO_MID, ActionType.MID_TO_LEFT, mid_stack, left_stack, MID, LEFT)
        step_count += process_by_stack(curr_action, ActionType.RIGHT_TO_MID, ActionType.MID_TO_RIGHT, mid_stack,
                                       right_stack, MID, RIGHT)
        step_count += process_by_stack(curr_action, ActionType.MID_TO_RIGHT, ActionType.RIGHT_TO_MID, right_stack, mid_stack, RIGHT, MID)

    print(step_count)



if __name__ == '__main__':
    # print(hanoi_by_re(3))
    print("==============================")
    print(hanoi_by_stack(3))