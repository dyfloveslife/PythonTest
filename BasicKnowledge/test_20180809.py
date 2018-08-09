# sum = 0
# x = 1
# while x < 100:
#     sum += x
#     x += 2
# print(sum)
#
# sum = 0
# i = 0
# while True:
#     if i >= 20:
#         break
#     sum += 2 ** i
#     i += 1
#
# print(sum)

# for x in range(10):
#     for y in range(10):
#         if x < y:
#             print('%d%d' % (x, y))
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for key in ['Adam', 'Lisa', 'Bart']:
    print('%s:%d' % (key, d[key]))
