import logging
import math

LOG_FORMAT = '%(levelname)s %(asctime)s - %(name)s - %(message)s'
# 增加以及初始化logger
logging.basicConfig(filename='f:\\Python_test\\BasicKnowledge\\test.log',
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger('carol')


# 测试logger
# logger.info('Our SECOND message.')
# print(logger.level)

def quadratic_formula(a, b, c):
    """
    Return the solutions to the equation ax^2 + bx + c = 0.
    """
    logger.info('quadratic_formula({0}, {1}, {2})'.format(a, b, c))

    # compute the discriminant
    logger.debug('# Compute the discriminant')
    disc = b ** 2 - 4 * a * c

    # compute the two roots
    logger.debug('# compute the two roots')
    root1 = (-b + math.sqrt(disc)) / (2 * a)
    root2 = (-b - math.sqrt(disc)) / (2 * a)

    # return the roots
    logger.debug('# return the roots')
    return root1, root2


roots = quadratic_formula(1, 0, -4)
print(roots)
