# def fib(n):
#     '''Print a Fibonacci series up to n.'''
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#     print()
#
#
# fib(100)

# def fib2(n):
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         # result = result + [a]
#         a, b = b, a + b
#     return result
#
#
# f100 = fib2(100)
# print(f100)


# def ask_ok(prompt, reties=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         reties = reties - 1
#         if reties < 0:
#             raise ValueError('invalid user response')
#         print(reminder)
#
#
# # ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

#

# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L
#
#
# print(f(1))
# print(f(2))
# print(f(3))
'''必需的参数voltage和三个可选参数'''


#
#
# def parrot(voltage, state='a stiff', action='voom ', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end='')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage,the", type)
#     print("--It's", state, "!")
#
#
# # parrot(1000)
# # parrot(voltage=1000)
# # parrot(voltage=1000, action='VOOOOOOM ')
# # parrot(action='VOOOOOOM ', voltage=100000000)
# # parrot('a', 'b', 'c ')
# # parrot('a thousand', state='pushing up the daisies')
# parrot(110, 220)

def cheeseshop(kind, *arguments, **keywords):
    print("--Do you have any", kind, "?")
    print("--I'm sorry,we're all out of", kind)
    for i in arguments:
        print(i)
        keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny,sir.",
           "It's really very,VERY runny,sir.,",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

'''从4.7.3开始学习'''