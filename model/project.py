__author__ = 'IEUser'


class Project:
    def __init__(self, name="", description=""):
        self.name = name
        self.description = description

    def __repr__(self):
        return "%s : %s" % (self.name, self.description)

    def __eq__(self, other):
        return self.name == other.name \
            and self.description == other.description

    def name(self):
        return self.name
