class queue:
    def __init__(self):
        self.queue = list ()
    def addque(self,data):
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        return False
    def size (self):
        return len(self.queue)
thequeue = queue ()
print(thequeue.addque('data science'))
print(thequeue.addque('big data'))
print(thequeue.addque('IoT'))
print(thequeue.addque('machine learning'))
print(thequeue.addque('deep learning'))
print(thequeue.size())