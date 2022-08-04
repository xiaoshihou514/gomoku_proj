import compute


def resolve_pattern_jump(pattern):
    # Check if there's a jump_three, four or five
    if pattern[0] == 1 and pattern[1] == 1:
        return compute.JUMP_FIVE
    elif pattern[0] == 1:
        return compute.JUMP_FOUR
    else:
        return compute.JUMP_THREE


def resolve_pattern_jump_rev(pattern):
    # Check if there's a jump_three, four or five
    if pattern[0] == 2 and pattern[1] == 2:
        return compute.JUMP_BLOCKED_THREE
    elif pattern[0] == 2:
        return compute.JUMP_BLOCKED_TWO
    else:
        return 0

# Winning conditions
FIVE = [1,1,1,1,1] # len 5
FOUR = [0,1,1,1,1,0] # len 6
# Hooks
JUMP_FIVE_D1 = [1,1,1,0,1] # len 5
JUMP_FIVE_D2 = [1,0,1,1,1]
JUMP_FIVE_D3 = [1,1,0,1,1]
JUMP_FOUR_D1 = [0,1,1,0,1,0] # len 6
JUMP_FOUR_D2 = [0,1,0,1,1,0]
BLOCKED_FOUR_D1 = [2,1,1,1,1,0] # len 6
BLOCKED_FOUR_D2 = [0,1,1,1,1,2]
THREE = [0,1,1,1,0] # len 5
# Minors
JUMP_THREE_D1 = [0,1,1,0,1,0] # len 6
JUMP_THREE_D2 = [0,1,0,1,1,0]
TWO = [0,1,1,0] # len four
BLOCKED_THREE_D1 = [2,1,1,1,0] # len 5
BLOCKED_THREE_D2 = [0,1,1,1,2]
JUMP_BLOCKED_TWO_D1 = [2,0,1,1,0] # len 5
JUMP_BLOCKED_TWO_D2 = [0,1,1,0,2]
JUMP_BLOCKED_THREE_D1 = [2,0,1,1,1,0] # len 6
JUMP_BLOCKED_THREE_D2 = [0,1,1,1,0,2] # len 6
BLOCKED_TWO_D1 = [2,1,1,0] # len 4
BLOCKED_TWO_D2 = [1,1,2,0]
def resolve_pattern_cont(pattern):
    final_score = 0
    for i in range(0,10):
