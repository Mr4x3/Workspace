class Reader():
    def __init__(self, file):
        self.file=file
        self.f=open(self.file,'r')

    def close(self):
        self.f.close()
    def read(self):

        return self.f.read()
