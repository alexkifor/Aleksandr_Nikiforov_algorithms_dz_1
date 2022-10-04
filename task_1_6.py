class TaskBoard:
    def __init__(self, base_queue, revision_queue):
        self.base_queue = base_queue
        self.revision_queue = revision_queue
        self.result = []

    def to_base_queue(self, item):
        self.base_queue.insert(0, item)

    def from_base_queue_to_result(self):
        task = self.base_queue.pop()
        self.result.append(task)

    def to_revision_task(self):
        task = self.base_queue.pop()
        self.revision_queue.insert(0, task)

    def from_revision_to_base_queue(self):
        task = self.revision_queue.pop()
        self.base_queue.insert(0, task)

    def from_revision_to_result(self):
        task = self.revision_queue.pop()
        self.result.append(task)


task_board = TaskBoard(base_queue=[], revision_queue=[])
task_board.to_base_queue('first')
task_board.to_base_queue('second')
task_board.to_base_queue('third')
print(task_board.base_queue)                                 # ['third', 'second', 'first']
task_board.from_base_queue_to_result()
print(task_board.result)                                     # ['first']
print(task_board.base_queue)                                 # ['third', 'second']
task_board.to_revision_task()
print(task_board.revision_queue)                             # ['second']
print(task_board.base_queue)                                 # ['third']
task_board.to_revision_task()
print(task_board.base_queue)                                 # []
print(task_board.revision_queue)                             # ['third', 'second']
task_board.from_revision_to_result()
task_board.from_revision_to_base_queue()
task_board.from_base_queue_to_result()
print(task_board.result)                                     # ['first', 'second', 'third']

