import threading
from queue import Queue
from enum import Enum
from cutlery import Cutlery, kitchen

class BotTasks(Enum):
    PREPARE = 'prepare_table'
    CLEAR = 'clear_table'
    SHUTDOWN = 'shutdown'


class ThreadBot(threading.Thread):
    def __init__(self):
        super().__init__(target=self.manage_table)
        self.cutlery = Cutlery(knives=0, forks=0)
        self.tasks = Queue()
    
    def manage_table(self) -> None:
        while True:
            task = self.tasks.get()
            if task == BotTasks.PREPARE:
                kitchen.give(to=self.cutlery, knives=4, forks=4)
            elif task == BotTasks.CLEAR:
                self.cutlery.give(to=kitchen, knives=4, forks=4)
            elif task == BotTasks.SHUTDOWN:
                return
