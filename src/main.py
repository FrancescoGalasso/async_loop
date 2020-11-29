# coding: utf-8

# pylint: disable=missing-docstring
# pylint: disable=logging-fstring-interpolation
# pylint: disable=attribute-defined-outside-init

import asyncio
import logging
import sys

from random import randint


class LoopApp():

    def __init__(self):

        self.__version = None
        self.__tasks = []

        self.__init_tasks()

    def __init_tasks(self):

        self.__tasks = []

        # create fast task
        fast_task = self.__create_fast_task(1)
        self.__tasks.append(fast_task)

        # create slow task
        slow_task = self.__create_slow_task(5)
        self.__tasks.append(slow_task)

        # https://docs.python.org/3.8/library/asyncio-task.html#coroutines
        logging.info(f"self.__tasks:{self.__tasks}")

    def __close_tasks(self):
        # https://docs.python.org/3.8/library/asyncio-task.html#asyncio.Task.cancel

        logging.debug('close all tasks')

        for t in self.__runners[:]:
            logging.debug(f'task type: {type(t)}')
            logging.debug(f'closing task {t}')
            try:
                t.cancel()

                async def _coro(_):
                    await _
                asyncio.get_event_loop().run_until_complete(_coro(t))
            except asyncio.CancelledError:
                logging.info(f"{ t } has been canceled now.")

        self.__runners = []

    async def __create_fast_task(self, sleep_time=1):
        while True:
            random_value = randint(1, 10)
            logging.info(f'[FAST TASK] - random number: {random_value}')
            await asyncio.sleep(sleep_time)

    async def __create_slow_task(self, sleep_time=5):
        while True:
            random_value = randint(100, 200)
            logging.info(f'[SLOW TASK] - random number: {random_value}')
            await asyncio.sleep(sleep_time)

    def get_version(self):

        if not self.__version:
            self.__version = '0.0.1'
        return self.__version

    def run(self):

        # https://docs.python.org/3.8/library/asyncio-future.html#asyncio.ensure_future
        # https://docs.python.org/3.8/library/asyncio-eventloop.html#asyncio.get_event_loop
        # https://docs.python.org/3.8/library/asyncio-eventloop.html#asyncio.loop.run_forever

        try:
            self.__runners = [asyncio.ensure_future(t) for t in self.__tasks]
            self.loop = asyncio.get_event_loop()
            self.loop.run_forever()

        except KeyboardInterrupt:
            pass

        except Exception as e:        # pylint: disable=broad-except
            logging.error(e)

        finally:

            self.__close_tasks()

            self.loop.stop()
            self.loop.run_until_complete(self.loop.shutdown_asyncgens())
            self.loop.close()

def main():

    fmt_ = '[%(asctime)s]%(levelname)s %(funcName)s() %(filename)s:%(lineno)d %(message)s'
    logging.basicConfig(stream=sys.stdout, level='INFO', format=fmt_)

    app = LoopApp()
    logging.info(f"version: {app.get_version()} - Ctrl+C to close me.")
    app.run()


if __name__ == "__main__":
    main()
