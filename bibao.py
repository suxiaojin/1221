origin=0

# def go(step):
#     global origin
#     new_pos= origin + step
#     origin=new_pos
#     return origin
#
# print(go(2))
# print(go(3))
# print(go(6))


def factory(pos):
    def go(step):
        nonlocal pos
        new_pos=pos+step
        pos=new_pos
        return new_pos
    return go
tourist=factory(origin)
print(tourist(2))
print(tourist.__closure__)
print(tourist(3))
print(tourist(5))