s = open('in06.txt', 'r').readline().strip()


def sol1(s, sz=4):
    for i in range(len(s)-sz+1):
        p = s[i:i+sz]
        if len(set(p)) == len(p):
            return i+sz


assert sol1('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7
assert sol1('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
assert sol1('nppdvjthqldpwncqszvftbrmjlhg') == 6
assert sol1('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
assert sol1('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11

print(sol1(s))
print(sol1(s, sz=14))
