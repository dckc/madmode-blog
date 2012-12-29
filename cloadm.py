'''cloadm -- emulate coco CLOADM command

ref: The FACTS pg. 10

'''

__author__ = 'Dan Connolly'
__contact__ = 'http://www.madmode.com/'

import struct
import logging
import wave

import numpy

log = logging.getLogger(__name__)


def main(argv=None, level=logging.DEBUG):
    logging.basicConfig(level=level)
    if argv is None:
        import sys
        argv = sys.argv

    tape_fn, dest_fn = argv[1:3]
    tape = wave.open(tape_fn, 'r')
    decode(tape, open(dest_fn, 'w'))


class CoCo(object):
    '''A sine wave of 2400 hz is used to store a one,
    and a site wave of 1200 Hertz is used to store a zero.'''
    rate0 = 1200
    rate1 = 2400
    CMPMID = 18  # 1200/2400 HERTZ PARTITON per The Facts p.g A 3
    CMP0 = 24  # UPPER LIMIT OF 1200 HERTZ PERIOD per The Facts p.g A 3
    CMP1 = 10  # UPPER LIMIT OF 2400 HERTZ PERIOD per The Facts p.g A 3


def decode(tape, dest):
    framerate, signal = wavLoadMono(tape)
    freqs, wave_ix = waves(signal, framerate)
    threshold = 1400  # experimental; cf. (CoCo.rate0 + CoCo.rate1) / 2
    bits = (freqs > threshold) + 0

    namefile_block, offset = get_block(bits, leader=True)
    bits = bits[offset:]
    dest.write(namefile_block)

    block, offset = get_block(bits, leader=True)
    while len(block) > 0:
        dest.write(block)
        bits = bits[offset:]
        block, offset = get_block(bits, leader=False)


def get_block(bits, leader, sync_byte=0x3C, pattern=0x55):
    if leader:
        offset = find_sync(bits)
    else:
        _, offset = next_byte(bits, 0, expected=pattern,
                              label='block start')
        _, offset = next_byte(bits, offset, expected=sync_byte,
                              label='block start')

    block_type, offset = next_byte(bits, offset)
    block_length, offset = next_byte(bits, offset)
    log.info('block type: %d length: %d', block_type, block_length)
    if block_type not in (0x00, 0x01, 0xFF):
        raise ValueError(block_type)

    data, offset = next_bytes(bits, offset, block_length)
    check = (sum(data) + block_type + block_length) & 0xFF
    checksum, offset = next_byte(bits, offset, expected=check, label='check')
    sync, offset = next_byte(bits, offset, expected=pattern, label='block end')

    return data, offset


def find_sync(bits, qty=96, sync=0x3C):
    lo = 0
    eof = len(bits)
    max_seen = 0
    while 1:
        pattern, hi, target = initial_segment(bits, lo, qty)
        if hi - lo > max_seen:
            max_seen = hi - lo
            log.debug('%s * %d @ %d %s ...',
                      pattern, (hi - lo) / 2, lo, bits[lo:lo + 8])
        if target is not None and (pattern in (0x01, 0x02)):
            break
        lo = hi

    while hi + 8 <= eof:
        if binary(bits[hi:hi + 8])[0] == sync:
            return hi + 8
        hi += 1

    raise ValueError('no sync byte found')


def initial_segment(bits, lo, qty):
    pattern = binary(bits[lo:lo + 2], 2)[0]
    target = lo + qty * 2
    if target > len(bits):
        raise ValueError('no sync found')
    hi = lo + 2
    while 1:  # TODO: vectorize?
        if hi == target:
            return pattern, hi, target
        if binary(bits[hi - 2:hi], 2) != pattern:
            return pattern, hi - 2, None
        hi += 2


def waves(signal, framerate, amp_max=128):
    signal = signal * amp_max / max(signal)
    z = zero_crossings(signal)
    assert((numpy.sign(signal[z[::2]]) == numpy.sign(z[0])).all())
    z = z[:-(len(z) % 2 + 1)]  # odd # crossings gives even # half waves
    hw = numpy.diff(z)
    h0 = hw[::2]
    h1 = hw[1::2]
    periods = h0 + h1

    freqs = framerate * 1.0 / periods  # in hz
    #@@ filter_ix = numpy.where(freqs < max_freq)
    wave_sample = z[:len(freqs) * 2:2]
    return freqs, wave_sample


def zero_crossings(signal):
    '''
    ack: Jim Brissom Oct 1 2010
    http://stackoverflow.com/a/3843124

    >>> a = [1, 2, 1, 1, -3, -4, 7, 8, 9, 10, -2, 1, -3, 5, 6, 7, -10]
    >>> zero_crossings(a)
    array([ 3,  5,  9, 10, 11, 12, 15])

    Watch out for zero:

    >>> a = [2, 1, 0, -1, -2, 1, 4, -4]
    >>> zero_crossings(a)
    array([1, 4, 6])
    '''
    return numpy.where(numpy.diff(numpy.sign(signal) > 0))[0]


def binary(bits, width=8):
    '''
    Least significant first:
    >>> binary(numpy.array([0, 0, 0, 0, 1, 1, 1, 1,
    ...                     1, 1, 1, 1, 0, 0, 0, 0]))
    array([240,  15])

    >>> binary(numpy.array([0, 0, 0, 0, 1, 1, 1, 1,
    ...                     1, 1, 1, 1, 0, 0, 0, 0]), 2)
    array([0, 0, 3, 3, 3, 3, 0, 0])
    '''
    bitn = [bits[i::width] for i in range(0, width)]
    nbyte = min(map(len, bitn))
    values = sum([bitn[i][:nbyte] * (1 << i) for i in range(0, width)])
    return values.astype(numpy.uint8)


def next_byte(bits, offset, expected=None, label=None):
    o8 = offset + 8
    b = binary(bits[offset:o8])[0]

    if expected and b != expected:
        log.warn('expected %s $%x does not match found $%x',
                 label, expected, b)

    return b, o8


def next_bytes(bits, offset, count):
    oend = offset + 8 * count
    b = binary(bits[offset:oend])
    return b, oend


def wavLoadMono(wav):
    p = wav.getparams()
    (nchannels, sampwidth, framerate,
     nframes, comptype, _compname) = p
    if nchannels != 1:
        raise ValueError(nchannels)
    if sampwidth != 2:
        raise ValueError(sampwidth)
    if comptype != 'NONE':
        raise ValueError(comptype)
    frames = wav.readframes(nframes)
    out = struct.unpack_from("%dh" % nframes, frames)
    return framerate, numpy.array(out)


if __name__ == '__main__':
    main()
