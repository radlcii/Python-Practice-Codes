class Node:
    def _init_(self, data=None, link0=None, link1=None):
        self.data
        self.link0 = link0
        self.link1 = link1

    def get_data(self):
        return self.data
    
    def get_link0(self):
        return self.link0

    def get_link1(self):
        return self.link1

    def set_link0(self, newLink0):
        self.link0 = newLink0

    def set_link1(self, newLink1):
        self.link1 = newLink1