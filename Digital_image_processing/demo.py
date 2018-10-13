# import scipy.misc
#
# mat = scipy.misc.imread('xjpic.jpg')
# print(mat.shape)

# import PIL.Image
#
# im = PIL.Image.open('jp.jpg')
# r, g, b = im.split()
#
# r.show()
# g.show()
# b.show()

# import PIL.Image
#
# im = PIL.Image.open('xjpic.jpg')
# r, g, b = im.split()
# im = PIL.Image.merge('RGB', (b, g, r))
# im.show()


import PIL.Image
import scipy.misc
import numpy as np


def convert_3d(r):
    s = np.empty(r.shape, dtype=np.uint8)
    for j in range(r.shape[0]):
        for i in range(r.shape[1]):
            s[j][i] = (r[j][i] / 255) ** 0.67 * 255
    return s


im = PIL.Image.open('sample1.jpg')
im.show()
im_mat = scipy.misc.fromimage(im)
im_converted_mat = convert_3d(im_mat)
im_converted = PIL.Image.fromarray(im_converted_mat)
im_converted.show()