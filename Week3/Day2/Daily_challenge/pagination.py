class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items
        self.pageSize = pageSize
        self.pages_count = (len(self.items) + self.pageSize - 1) // self.pageSize
        self.current_page = 0

    def getVisibleItems(self):
        start_page = self.current_page * self.pageSize 
        try:
            print(self.items[start_page : start_page + self.pageSize])
        except:
            print(self.items[start_page : ])

    def firstPage(self):
        self.current_page = 0
        return self

    def nextPage(self):
        if self.current_page < (self.pages_count - 1):
            self.current_page += 1
        return self   

    def lastPage(self):
        self.current_page = self.pages_count - 1 
        return self

    def prevPage(self):
        if self.current_page > 0:
            self.current_page -= 1
        return self 

    def goToPage(self, pageNum):
        if 1 <= pageNum <= self.pages_count:
            self.current_page = pageNum - 1
        elif pageNum == 0:
            self.current_page = 0
        else:    
            self.current_page = self.pages_count - 1  
        return self  

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
# abcdefg hijklmn opqrstu vwxyz

p = Pagination(alphabetList, 7)

p.goToPage(3).prevPage().prevPage().prevPage().prevPage().getVisibleItems()
p.lastPage().getVisibleItems()
p.firstPage().nextPage().getVisibleItems()


 
              
        
                           



        