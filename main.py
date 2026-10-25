def send_message(self):
    txt = self.screen.ids.input_field.text.strip()
    if txt == "":
        return
    self.add_msg("Tu: " + txt)
    self.screen.ids.input_field.text = ""

    lower = txt.lower()
    # Detectar idioma por palabras comunes
    english_words = ["how", "tank", "fish", "water", "photo", "what", "is", "my"]
    portuguese_words = ["como", "meu", "tanque", "peixe", "água", "foto", "está", "voce", "você"]

    if any(w in lower for w in english_words):
        # INGLES
        if "tank" in lower or "fish" in lower:
            self.add_msg("AcuarioApp: You have 3 tanks. Main Reef 220L is stable.")
        elif "photo" in lower:
            self.add_msg("AcuarioApp: Tap the + to send a photo.")
        else:
            self.add_msg("AcuarioApp: Got it! I saved it in your tasks.")
    elif any(w in lower for w in portuguese_words):
        # PORTUGUES
        if "tanque" in lower or "peixe" in lower:
            self.add_msg("AcuarioApp: Você tem 3 tanques. Main Reef 220L está estável.")
        elif "foto" in lower:
            self.add_msg("AcuarioApp: Toque no + para mandar uma foto.")
        else:
            self.add_msg("AcuarioApp: Entendido! Salvei nas suas tarefas.")
    else:
        # ESPAÑOL por defecto
        if "tanque" in lower:
            self.add_msg("AcuarioApp: Tienes 3 tanques. Main Reef 220L esta estable.")
        elif "foto" in lower:
            self.add_msg("AcuarioApp: Toca el + para mandar una foto.")
        else:
            self.add_msg("AcuarioApp: Entendido! Lo anoto en tus tareas.")
