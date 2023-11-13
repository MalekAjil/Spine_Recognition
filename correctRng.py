from numpy import uint8
from numpy.core.numerictypes import cast


def correctRng(imm):
    mx = max(max(imm))
    mn = min(min(imm))
    #
    # if (mn < 0) | (mx > 255):
    #     im1 = mat2gray(imm)
    #     img = uint8(im1 * 255)
    #
    # elif (mn >= 0) & (mx < 255):
    y = ((imm[:, :] - min) * 255 / (max - min))
    imm = imm[:, :] - mn
    rng = (255 / (mx - mn))
    img = round(imm * rng)
    img = cast(img, 'uint8')

    # imshow(img)
    # im2=uint8(imm)
    # im3=histeq(im2)
    # montage({imm,im1,img,im2,im3})
    return img
