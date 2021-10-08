# f = open("log.txt", "w")
q = input().strip()
# q = "mobitel"

# brute force
l = len(q)
word = "".join(reversed(q[0:1])) + "".join(reversed(q[1:2])) + "".join(reversed(q[2:]))

for i in range(1, l - 1):
    for j in range(i + 1, l):
        temp = (
            "".join(reversed(q[0:i]))
            + "".join(reversed(q[i:j]))
            + "".join(reversed(q[j:]))
        )

        if temp <= word:
            word = temp
            # f.write(f"NEW! => {temp} {i}_{j}\n")
        # else:
        # f.write(f"{temp} {i}_{j}\n")

print(word)
