class ESuite(object):
    def __repr__(self):
        return '%s(...)' % self.__class__.__name__

    @classmethod
    def lift_doc(cls, suite):
        for n, f in suite.items():
            setattr(cls, n, f)

    @classmethod
    def make(cls, *args, **kwargs):
        suite = dict(dict([(f.__name__, f) for f in args]),
                     **kwargs)
        suite_ld = dict(suite, lift_doc=lambda _: cls.lift_doc(suite))
        return type(cls.__name__, (ESuite, object), suite_ld)()
