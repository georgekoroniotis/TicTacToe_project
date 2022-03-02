class Player:

    def __init__(self, name):
        self.name = name
        self.marker = None

    def __str__(self):
        return "The player is {}".format(self.name)

    def set_marker(self, marker):
        self.marker = marker

    def get_marker(self):
        return self.marker

    def check_marker(self, marker):
        if self.marker == marker:
            return True
        else:
            return False

