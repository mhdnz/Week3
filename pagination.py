class Pagination(object):

    def __init__(self, items: list, page_size: float = 10):
        self.items = items
        self.page_size = int(page_size)
        self.current = 0

    def prevPage(self):
        if self.current > 0:
            self.current -= 1
        return self

    def nextPage(self):
        if self.current < len(self.items)//self.page_size:
            self.current += 1
        return self

    def fisrtPage(self):
        self.current = 0
        return self

    def lastPage(self):
        self.current = len(self.items)//self.page_size
        return self

    def goToPage(self, index: float):
        idx = int(index)
        if 0 < idx < len(self.items)//self.page_size:
            self.current = idx
        elif idx < 0 :
            self.fisrtPage()
        else:
            self.lastPage()
        return self

    def getVisibaleItems(self):
        begin = self.page_size*self.current
        end = min(begin + self.page_size, len(self.items))
        page_items = []
        for i in range(begin, end):
            page_items.append(self.items.__getitem__(i))
        return page_items


if __name__ == '__main__':
    pi = Pagination(list("abcdefghijklmonpqrstuvwxyz"), 4)
    print(pi.getVisibaleItems())
    pi.nextPage()
    print(pi.getVisibaleItems())
    pi.nextPage()
    print(pi.getVisibaleItems())
    pi.nextPage()
    print(pi.getVisibaleItems())
    pi.nextPage()
    print(pi.getVisibaleItems())
    pi.nextPage()
    print(pi.getVisibaleItems())
    pi.prevPage()
    print(pi.getVisibaleItems())
    pi.fisrtPage()
    print(pi.getVisibaleItems())
    pi.prevPage()
    print(pi.getVisibaleItems())
    pi.lastPage()
    print(pi.getVisibaleItems())
    pi.nextPage()
    print(pi.getVisibaleItems())
    pi.prevPage()
    print(pi.getVisibaleItems())
    pi.goToPage(1)
    print(pi.getVisibaleItems())
    pi.goToPage(-1)
    print(pi.getVisibaleItems())
    pi.goToPage(110)
    print(pi.getVisibaleItems())
    pi.prevPage().nextPage()
    print(pi.getVisibaleItems())
