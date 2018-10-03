import datetime
class Batch:
    def __init__(self,batchID,actualPrice,quantity,shelfDate, shelfLife):
        self.batchID = batchID
        self.shelfDate = shelfDate
        self.actualPrice = actualPrice
        self.quantity = quantity
        self.setExpiryDate(shelfLife)
        self.shelfLife = shelfLife


    def generateActualPrice(self):
        pass

    def getActualPrice(self):
        return self.actualPrice

    def getBatchID(self):
        return self.batchID

    def getDiscount(self):
        if self.expiryDate - self.shelfDate > datetime.timedelta(days = 7):
            return 1.0
        else:
            return 0.3 + 0.6 * ((self.expiryDate - self.shelfDate).days / 7)

    def getExpiryDate(self):
        return self.expiryDate

    def getShelfDate(self):
        return self.shelfDate

    def getQuantity(self):
        return self.quantity

    def setActualPrice(self, actualPrice):
        self.actualPrice = actualPrice

    def setBatchId(self,batchID):
        self.batchID = batchID

    def setExpiryDate(self, daysTilExpiry):
        self.expiryDate = self.shelfDate + datetime.timedelta(days= daysTilExpiry)

    def setShelfDate(self, shelfDate):
        self.shelfDate = shelfDate

    def setQuantity(self, quantity):
        self.quantity = quantity

if __name__ == '__main__':
    bs = [Batch(23, 1.00, 20, datetime.date.today(), i) for i in range(0, 10)]
    for b in bs:
        print(b.getDiscount())
