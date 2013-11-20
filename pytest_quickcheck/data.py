from generator import parse, generate, Generator, get_int


def do_generate(data, **kwargs):
    data_type, retrieve = parse(data)
    return retrieve(generate(data_type, **kwargs))

class listof(Generator):
    def __init__(self, data, **options):
        self.data = data
        self.min_num = options.pop("min_num", 0)
        assert self.min_num >= 0
        self.max_num = options.pop("max_num", 20)
        self.options = options

    def generate(self, **kwargs):
        kwargs.update(self.options)
        k = get_int(self.min_num, self.max_num)
        return [do_generate(self.data, **kwargs) for _ in xrange(k)]

def listof1(data, **options):
    options.setdefault("min_num", 1)
    return listof(data, **options)