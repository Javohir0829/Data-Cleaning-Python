class FrameModel:
    def __init__(self, name, properties):
        self.name = name
        self.properties = properties

    def display(self):
        print(f"--- Freym modeli ({self.name}) ---")
        for key, value in self.properties.items():
            print(f"  {key}: {value}")

class ProductionModel:
    @staticmethod
    def check_rule(condition):
        if "kasal" in condition:
            return "Natija: Shifokor ko'rigidan o'tish tavsiya etiladi."
        elif "sog'lom" in condition:
            return "Natija: Profilaktika uchun vitaminlar qabul qiling."
        return "Natija: Ma'lumot yetarli emas."

def logical_decision(score):
    if score >= 60:
        return "Mantiqiy xulosa: Imtihondan o'tdi."
    return "Mantiqiy xulosa: Qayta topshirish kerak."


# Freymga misol (Avtomobil xususiyatlari)
car_frame = FrameModel("Avtomobil", {"Marka": "Chevrolet", "Model": "Gentra", "Yil": 2024})
car_frame.display()

print("\n--- Produksion model ---")
status = "bemor kasal"
print(f"Holat: {status} -> {ProductionModel.check_rule(status)}")

# Mantiqiy modelga misol
print("\n--- Mantiqiy model ---")
student_score = 75
print(f"Ball: {student_score} -> {logical_decision(student_score)}")