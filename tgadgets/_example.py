# coding=utf-8
"""

v1.0.0 Initial

Simple test examples:
1. get_files_list test
2. Timer test
3. MpProgress test for: a. map_async; b. apply_async

"""
import os
from multiprocessing import freeze_support, Pool
from time import sleep

from tgadgets import file as fl
from tgadgets import progress as pg


def test_get_files_list(test_dir):
    print("Created files for testing.")
    for fn in range(100):
        with open(test_dir + r'\test_file_%03i.tst' % fn, mode='a') as tf:
            tf.write('test')

    file_pattern = dict(path=test_dir,
                        file_init='test_file',
                        file_ext='.tst')
    test_files_list = fl.get_files_list(**file_pattern)

    def clean_files(files_list):
        for file in files_list:
            os.remove(file['path'])

    clean_files(test_files_list)
    print("Cleaned testing files.")
    fl.get_files_list(**file_pattern)


def test_timer():
    timer_test = pg.Timer()
    timer_test.start("Testing Timer", "Action I")
    print("--| Sleep for 1 second.")
    sleep(1)
    timer_test.switch("Action II")
    print("--| Sleep for 2 seconds.")
    sleep(2)
    timer_test.stop()


def test_func(x):
    return 1 / x


def test_mp():
    test_data = list(range(1, 100000))
    timer_mp = pg.Timer()

    timer_mp.start("Testing MpProgress", "Initializing")
    with Pool(os.cpu_count() // 2) as test_pool:
        timer_mp.switch("Testing 'map_async'")
        map_result = test_pool.map_async(test_func, test_data)
        mp_test_map = pg.MpProgress(map_result, 'map')
        mp_test_map.show()
        print("--| Result = %i" % sum(map_result.get()))

        timer_mp.switch("Testing 'apply_async'")
        apply_results = [test_pool.apply_async(test_func, (test_datum,)) for test_datum in test_data]
        mp_test_apply = pg.MpProgress(apply_results, 'apply')
        mp_test_apply.show()
        print("--| Result = %i" % sum([apply_result.get() for apply_result in apply_results]))

    timer_mp.stop()


if __name__ == '__main__':
    freeze_support()
    test_get_files_list(os.getcwd())
    test_timer()
    test_mp()
