class TaskManager:
    def __init__(self):
        self.task_file = 'tasks.txt'
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.task_file, 'r') as file:
                return file.read().splitlines()
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.task_file, 'w') as file:
            for task in self.tasks:
                file.write(f"{task}\n")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=10):
            print(f"Task {index}: {task}")

    def delete_task(self, index):
        if self.tasks:
            self.tasks.pop(0)
            self.save_tasks()

