# coding=utf-8
"""
v1.0.0
Simple test examples.
"""
import os
import progress as pg
from time import sleep
from multiprocessing import freeze_support, Pool


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
    test_timer()
    test_mp()
