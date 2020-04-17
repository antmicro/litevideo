from migen import *

from litex.soc.interconnect import stream


def saturate(i, o, minimum, maximum, dw):
    return [
        If(i[-1] == 1,
            o.eq(minimum)
        ).Elif(i > maximum,
            o.eq(maximum)
        ).Else(
            o.eq(i[:dw])
        )
    ]


def coef(value, cw=None):
    return int(value * 2**cw) if cw is not None else value

def rgb_layout(dw):
    return [("r", dw), ("g", dw), ("b", dw)]

def rgb16f_layout(dw):
    return [("rf", dw), ("gf", dw), ("bf", dw)]

def ycbcr444_layout(dw):
    return [("y", dw), ("cb", dw), ("cr", dw)]

def ycbcr422_layout(dw):
    return [("y", dw), ("cb_cr", dw)]

def pix_layout(dw):
    return [("pix", dw)]

def pixf_layout(dw):
    return [("pixf", dw)]

