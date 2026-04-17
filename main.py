# 50. Sayohat vaqtlari

class Travel:
    def __init__(self, transport_type, duration_hours):
        self.transport_type = transport_type    # "Samolyot", "Poezd", "Avtobus" va h.k.
        self.duration = duration_hours          # sayohat vaqti (soat)

    def get_duration(self):
        """Sayohat davomiyligi (soat)"""
        return self.duration

    def __str__(self):
        return f"{self.transport_type:14} | {self.duration:5.1f} soat"


# -----------------------------------------------
# Voris sinflar (emoji va chiroyli format bilan)
# -----------------------------------------------

class FlightTravel(Travel):
    def __str__(self):
        dur = self.get_duration()
        return f"✈️ {self.transport_type:12} → {dur:5.1f} soat"


class TrainTravel(Travel):
    def __str__(self):
        dur = self.get_duration()
        return f"🚂 {self.transport_type:12} → {dur:5.1f} soat"


# Qo‘shimcha variantlar (foydali bo‘lishi mumkin)
class BusTravel(Travel):
    def __str__(self):
        dur = self.get_duration()
        return f"🚌 {self.transport_type:12} → {dur:5.1f} soat"


# --------------------------------------------------
# Sayohat vaqtlarini chiqarish
# --------------------------------------------------

def show_travel_durations(travels):
    print("\n" + "═" * 60)
    print("       SAYOHAT VAQTLARI — TRANSPORT TURLARI       ".center(60))
    print("═" * 60)
    print("Transport turi           Davomiylik (soat)")
    print("─" * 60)

    total_hours = 0

    for travel in travels:
        print(travel)
        total_hours += travel.get_duration()

    hours = int(total_hours)
    minutes = int((total_hours - hours) * 60)

    print("─" * 60)
    print(f"JAMI SAYOHAT VAQTI:              {hours:2} soat {minutes:02d} daqiqa")
    print("═" * 60 + "\n")


# Test ma'lumotlari
sayohatlar = [
    FlightTravel("Samolyot (Toshkent–Dubay)", 3.5),
    TrainTravel("Poezd (Toshkent–Samarqand)", 4.2),
    FlightTravel("Samolyot (Toshkent–Istanbul)", 5.1),
    BusTravel("Avtobus (Toshkent–Andijon)", 6.8),
    TrainTravel("Tezyurar poezd (Toshkent–Buxoro)", 3.8),
]

show_travel_durations(sayohatlar)


# Sizning misol qiymatlaringiz bilan:
print("\nSizning misol sayohatlaringiz:\n")
misol_sayohatlar = [
    FlightTravel("Samolyot", 2),
    TrainTravel("Poezd", 5),
]

show_travel_durations(misol_sayohatlar)
