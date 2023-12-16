class Gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
    
    def dampak(self):
        if self.skala < 2:
            print("Gempa di",self.lokasi, "dengan besar", self.skala, "tidak berdampak " )
        elif 2 <= self.skala < 4:
            print('Gempa di',self.lokasi, 'dengan besar',self.skala,"menyebabkan bangunan retak retak")
        elif 4 <= self.skala < 6:
            print('Gempa di',self.lokasi, 'dengan besar',self.skala,"menyebabkan bangunan roboh")
        else:
            print('Gempa di',self.lokasi, 'dengan besar',self.skala,"menyebabkan bangunan roboh dan berpotensi tsunami")

