# coding=utf-8
"""
v2.0.0
New TMapProgress and TApplyProgress for showing map_async and apply_async progress respectively, replacing old
    MpProgress which takes result_type as argument.

Test example codes are packed in the same file, with TLogger implemented for testing. The "if __name__ == '__main__'"
    clause ensures that example would not run by module importing.

"""
from time import time, sleep


class TMpProgress:
    def __init__(self, result_object):
        self.result = result_object
        self.progress = 0
        self.output = 0
        self.start_time = time()
        self.remain = self.total = None  # override below

    def _check_progress(self):
        pass  # override below

    def _show_remain_time(self):
        if self.progress == 0:
            return
        elapsed_time = time() - self.start_time
        remain_time = elapsed_time / self.progress * self.remain
        print("...%i seconds remaining..." % remain_time, end='')

    def _show_progress(self):
        percentage_5 = self.progress / self.total * 100 // 5 * 5
        print("\r--| %3i%%" % percentage_5, end='')

    def show(self):
        while self.remain > 0:
            self._check_progress()
            self._show_progress()
            if self.output % 10 == 0:
                self._show_remain_time()
            sleep(0.2)
            self.output += 1
        else:
            self._show_progress()
            print("...Finished.", end='')
            print()


class TMapProgress(TMpProgress):
    def __init__(self, result_object):
        super().__init__(result_object)
        self.remain = self.total = self.result.__getattribute__('_number_left')

    def _check_progress(self):
        self.remain = self.result.__getattribute__('_number_left')
        self.progress = self.total - self.remain


class TApplyProgress(TMpProgress):
    def __init__(self, result_object):
        super().__init__(result_object)
        self.remain = self.total = len(self.result)

    def _check_progress(self):
        self.progress = 0
        for async_result in self.result:
            if async_result.ready():
                self.progress += 1
                self.remain = self.total - self.progress


'''####################################
Test example code.
####################################'''
if __name__ == '__main__' or '__mp_main__':
    class TestProject:
        def __init__(self):
            self.logger = TLogger(separated=True)
            self.test_data = list(range(1, 100000))

        @staticmethod
        def _test_func(x):
            return 1 / 2 ** x

        def test(self):
            @self.logger.log_process('mp_test')
            def process():
                self._map_test()
                self._apply_test()

            process()

        def _map_test(self):
            @self.logger.log_action('map_async')
            def action():
                with Pool(os.cpu_count() // 2) as test_pool:
                    map_result = test_pool.map_async(self._test_func, self.test_data)
                    mp_test_map = TMapProgress(map_result, )
                    mp_test_map.show()
                    self.logger.log_msg("Result = %i" % sum(map_result.get()))

            action()

        def _apply_test(self):
            @self.logger.log_action('apply_async')
            def action():
                with Pool(os.cpu_count() // 2) as test_pool:
                    apply_results = [test_pool.apply_async(self._test_func, (test_datum,)) for test_datum in
                                     self.test_data]
                    mp_test_apply = TApplyProgress(apply_results)
                    mp_test_apply.show()
                    self.logger.log_msg("Result = %i" % sum([apply_result.get() for apply_result in apply_results]))

            action()


    if __name__ == '__main__':
        from tgadgets.logger import TLogger
        from multiprocessing import Pool, freeze_support
        import os

        freeze_support()
        test_project = TestProject()
        test_project.test()
