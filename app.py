import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()

app.geometry("800x500")
app.title("Meu Primeiro App")

titulo = ctk.CTkLabel(
    app,
    text="Meu Primeiro Sistema em Python!",
    font=("Arial", 24)
)

titulo.pack(pady=20)

botao = ctk.CTkButton(
    app,
    text="Entrar"
)

botao.pack(pady=20)

app.mainloop()
