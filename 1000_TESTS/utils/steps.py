class TestRecorder:
    def __init__(self, tc_id, name, module, file_relpath):
        self.tc_id = tc_id
        self.name = name
        self.module = module
        self.file_relpath = file_relpath
        self.steps = []
        self.stacktrace = None
        self.exception_type = None

    def step(self, msg):
        self.steps.append(msg)
