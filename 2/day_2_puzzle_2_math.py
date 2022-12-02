import Reader


answer = sum([(lambda a, b: (ord(b) + ord(a) - 154) % 3 + 3 * ord(b) - 263)(*r.split(" ")) for r in Reader.read("input")])
print(answer)

