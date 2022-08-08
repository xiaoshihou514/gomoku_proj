str = """
      
# Winning conditions
FIVE_REV = [1, 1, 1, 1, 1]  # len 5
FOUR_REV = [0, 1, 1, 1, 1, 0]  # len 6
# Hooks
JUMP_FIVE_D1_REV = [1, 1, 1, 0, 1]  # len 5
JUMP_FIVE_D2_REV = [1, 0, 1, 1, 1]
JUMP_FIVE_D3_REV = [1, 1, 0, 1, 1]
JUMP_FOUR_D1_REV = [0, 1, 1, 0, 1, 0]  # len 6
JUMP_FOUR_D2_REV = [0, 1, 0, 1, 1, 0]
BLOCKED_FOUR_D1_REV = [2, 1, 1, 1, 1, 0]  # len 6
BLOCKED_FOUR_D2_REV = [0, 1, 1, 1, 1, 2]
THREE_REV = [0, 1, 1, 1, 0]  # len 5
# Minors
JUMP_THREE_D1_REV = [0, 1, 1, 0, 1, 0]  # len 6
JUMP_THREE_D2_REV = [0, 1, 0, 1, 1, 0]
TWO_REV = [0, 1, 1, 0]  # len four
BLOCKED_THREE_D1_REV = [2, 1, 1, 1, 0]  # len 5
BLOCKED_THREE_D2_REV = [0, 1, 1, 1, 2]
JUMP_BLOCKED_TWO_D1_REV = [2, 0, 1, 1, 0]  # len 5
JUMP_BLOCKED_TWO_D2_REV = [0, 1, 1, 0, 2]
JUMP_BLOCKED_THREE_D1_REV = [2, 0, 1, 1, 1, 0]  # len 6
JUMP_BLOCKED_THREE_D2_REV = [0, 1, 1, 1, 0, 2]  # len 6

  """

print(str.replace("2","1").replace("1","2"))