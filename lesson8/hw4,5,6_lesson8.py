class OrgTekh(Exception):
    def __init__(self, name, count):
        self.name = name
        try:
            count = int(count)
        except Exception as error:
                print(error)
        else:
            self.count = count

class OrgTekhStock(OrgTekh):
    maxCount: int
    nowCount: int
    slovar = {}

    def __init__(self, count=5):
        self.maxCount = count
        self.nowCount = self.maxCount

    def store(self, tech: OrgTekh):
        if tech.count > self.nowCount:
            print("Мест на складе не хватит")
        else:
            self.nowCount = self.nowCount - tech.count
            self.slovar[tech.name] = f"{tech.count}"

    def infoStore(self):
        print(f"на складе занято {self.nowCount} мест из {self.maxCount} \n"
              f"Накладная: {self.slovar}")

printer = OrgTekh("Xeroh", 5)
sklad = OrgTekhStock(20)
sklad.store(printer)
sklad.infoStore()

scanner = OrgTekh("Scaner", 5)
sklad.store(scanner)
sklad.infoStore()

kopir = OrgTekh("Kopir", 11)
sklad.store(kopir)
sklad.infoStore()

lazerPrint = OrgTekh("lazer", "GG")