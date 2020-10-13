from kaitaistruct import KaitaiStream

import time
import random
import statistics

len_blob = 1 * (2 ** 10) # 1 kiB
num_sections = 2
num_iterations = 512

len_section = len_blob // num_sections

test_blob = bytes([i // len_section for i in range(len_blob)])

times = {f.__name__: [] for f in functions}

# https://www.peterbe.com/plog/how-to-do-performance-micro-benchmarks-in-python
for i in range(num_iterations):
    if i % 32 == 0:
        print(i)
    f_idx = random.randint(0, 1)

    t0 = time.time()
    if f_idx == 0:
        name = 'bytes_strip_right'
        KaitaiStream.bytes_strip_right(test_blob, 1)
    else:
        name = 'bytes_terminate'
        KaitaiStream.bytes_terminate(test_blob, 1, False)
    t1 = time.time()
    times[name].append((t1 - t0) * 1000)

for name, numbers in times.items():
    print('FUNCTION: {} Used {} times'.format(name, len(numbers)))
    print('\tMEDIAN {}'.format(statistics.median(numbers)))
    print('\tMEAN  {}'.format(statistics.mean(numbers)))
    print('\tSTDEV {}'.format(statistics.stdev(numbers)))
