def shoot(remains, index, info):
    need_to_win = info[index] + 1

    # win
    if remains >= need_to_win:
        shoot(remains - need_to_win, index + 1, info)

    # draw or loose
    if info[index] == 0:
        shoot(remains)
