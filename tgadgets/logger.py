# coding=utf-8
# coding=utf-8
"""
v2.0.0
A TLogger class replaces former Timer class with more convenient decorator methods and the ability to write log files.

Test example codes are packed in the same file, with TLogger implemented for testing. The "if __name__ == '__main__'"
    clause ensures that example would not run by module importing.
"""
from time import time, strftime, localtime


class TLogger:
    class Timer:
        def __init__(self) -> None:
            self.start_time = 0

        def start(self):
            self.start_time = time()

        @property
        def get(self) -> str:
            elapsed = str(round(time() - self.start_time, 2))
            self.__init__()
            return elapsed

    def __init__(self, separated: bool, log_path: str = ''):
        self._separated = separated
        self._process_timer = self.Timer()
        self._action_timer = self.Timer()
        self._log_path = log_path
        self._logs = []
        self._phase = 1

    def log_msg(self, *messages):
        if messages:
            for message in messages:
                self._log('--| {}\n'.format(message))

    def log_process(self, process_alias):
        def wrapper(process):
            def inner_wrapper(*args, **kwargs):
                if self._log_path:
                    with open(self._log_path, 'a') as log_file:
                        log_file.write(strftime('[%Y-%m-%d %H:%M]', localtime(time())))
                self._process_timer.start()
                self._log('\n>>> Starting [{}]\n'.format(process_alias))
                self._separate(2)
                process(*args, **kwargs)
                self._separate(2)
                self._log('### Finished [{}] in {} seconds\n\n'.format(process_alias,
                                                                       self._process_timer.get))

            return inner_wrapper

        return wrapper

    def log_action(self, action_alias):
        def wrapper(action):
            def inner_wrapper(*args, **kwargs):
                self._action_timer.start()
                self._log('{:0>2d}> Starting <{}>\n'.format(self._phase,
                                                            action_alias))
                self._separate(1)
                action(*args, **kwargs)
                self._separate(1)
                self._log('{:0>2d}# Finished <{}> in {} seconds\n'.format(self._phase,
                                                                          action_alias,
                                                                          self._action_timer.get))
                self._phase += 1

            return inner_wrapper

        return wrapper

    def _log(self, log_msg):
        if self._log_path:
            with open(self._log_path, 'a') as log_file:
                log_file.write(log_msg)
        print(log_msg, end='')

    def _separate(self, n_lines: int):
        if self._separated:
            self._log(n_lines * '---\n')


'''####################################
Test example code.
####################################'''
if __name__ == '__main__':
    from time import sleep


    class TestProject:
        def __init__(self):
            self.p1_logger = TLogger(separated=False, log_path='p1_log.txt')
            self.p2_logger = TLogger(separated=True, log_path='p1_log.txt')

        def process1(self):
            @self.p1_logger.log_process('process1')
            def process():
                self._action1_1()
                self._action1_2()

            process()

        def process2(self):
            @self.p2_logger.log_process('process2')
            def process():
                self._action2_1()
                self._action2_2()

            process()

        def _action1_1(self):
            @self.p1_logger.log_action('action1_1')
            def action():
                self.p1_logger.log_msg('Running action1')
                sleep(0.1)

            action()

        def _action1_2(self):
            @self.p1_logger.log_action('action1_2')
            def action():
                self.p1_logger.log_msg('Running action2')
                sleep(0.5)

            action()

        def _action2_1(self):
            @self.p2_logger.log_action('action2_1')
            def action():
                self.p1_logger.log_msg('Running action1')
                sleep(1)

            action()

        def _action2_2(self):
            @self.p2_logger.log_action('action2_2')
            def action():
                self.p1_logger.log_msg('Running action2')
                sleep(2)

            action()


    test_project = TestProject()
    test_project.process1()
    test_project.process2()
