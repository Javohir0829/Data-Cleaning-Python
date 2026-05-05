class TechExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            "ekran yoqilmayapti": "Quvvat blokini yoki monitorni ulovchi kabelni tekshiring.",
            "kompyuter sekin ishlayapti": "Protsessorni haddan tashqari qiziyotganini tekshiring yoki RAMni tozalang.",
            "internet yo'q": "Router sozlamalarini va tarmoq kabelini tekshiring.",
            "tovush chiqmayapti": "Drayverlar o'rnatilganini va karnay ulanishini tekshiring."
        }

    def diagnose(self, problem):
        problem = problem.lower()
        return self.knowledge_base.get(problem, "Kechirasiz, ushbu muammo bo'yicha bilimlar bazasida ma'lumot yo'q.")

expert = TechExpertSystem()

print("--- Texnik Diagnostika Ekspert Tizimi ---")
user_input = input("Muammoni kiriting (masalan, 'internet yo'q'): ")

result = expert.diagnose(user_input)
print(f"\nTizim tavsiyasi: {result}")