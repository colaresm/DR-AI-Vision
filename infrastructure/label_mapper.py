CLASS_LABELS = {
    2: "Saudável",
    0: "Leve",
    1: "Moderado",
    3: "Grave",
    4: "Proliferativa"
}

def get_label(class_number):
    return CLASS_LABELS.get(class_number, "Classe desconhecida")