def make_pretty_2d(matrix):
    # for str_list in matrix:
    #   str_list = ["{:3}".format(item) for item in row]
    #   new_row = " ".join(str_list)

    return "\n".join(
        [" ".join(["{:3}".format(item) for item in row]) for row in matrix]
    )
