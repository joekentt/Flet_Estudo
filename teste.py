# Mediador 
class Mediator:
    def notify(self, sender, event):
        pass

# Componentes
class TextBox:
    def __init__(self, mediator):
        self.mediator = mediator
        self.text = ""

    def set_text(self, text):
        self.text = text
        print(f"Texto inserido: {self.text}")
        self.mediator.notify(self, "text_changed")

class Button:
    def __init__(self, mediator):
        self.mediator = mediator
        self.enabled = False

    def click(self):
        if self.enabled:
            print("Botão clicado!")
        else:
            print("Botão desabilitado, insira o texto primeiro.")

    def set_enabled(self, enabled):
        self.enabled = enabled
        state = "habilitado" if enabled else "desabilitado"
        print(f"Botão {state}")

# Mediador concreto
class FormMediator(Mediator):
    def __init__(self, text_box, button):
        self.text_box = text_box
        self.button = button

    def notify(self, sender, event):
        if event == "text_changed":
            self.button.set_enabled(bool(self.text_box.text))

# Código de exemplo
text_box = TextBox(None)
button = Button(None)
mediator = FormMediator(text_box, button)
text_box.mediator = mediator
button.mediator = mediator

# Simulação
button.click()         # Botão desabilitado
text_box.set_text("Olá!")  # Texto inserido
button.click()         # Botão habilitado

text_box.set_text("")  # Remover o texto
button.click()  # O botão é desabilitado novamente
