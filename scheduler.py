class Task(dict):
    id = 0

    def __init__(self, s_time=None, e_time=None, title=None, content=None,
                    level=None, percent=None, users=set()):
        super().__init__()
        Task.id += 1
        self['id'] = Task.id
        self['s_time'] = s_time
        self['e_time'] = e_time
        self['title'] = title
        self['content'] = content
        self['level'] = level
        self['percent'] = percent
        self['users'] = users

    def match(self, keyword):
        if keyword in self['title'] or keyword in self['content']:
            return True
        else:
            return False
