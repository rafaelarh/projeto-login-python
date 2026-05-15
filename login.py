import customtkinter as ctk
from PIL import Image

# Configuração de aparência
ctk.set_appearance_mode("dark") 

app = ctk.CTk()
app.geometry("900x500")
app.title("Tela de Login")
app.configure(fg_color="#1a1a1a")

# Função do botão
def entrar():
    usuario = campo_usuario.get() 
    senha = campo_senha.get()

    if usuario == "rafaela" and senha == "1234":
        resultado.configure(text="Login realizado com sucesso!", text_color="green")
    else:
        resultado.configure(text="Usuário ou senha incorretos", text_color="red")

# --- 1. CARREGAR A IMAGEM (Lado Esquerdo) ---
imagem_banner = ctk.CTkImage(
    light_image=Image.open("banner.jpg"), 
    size=(450, 500) 
)

label_imagem = ctk.CTkLabel(app, image=imagem_banner, text="")
# Centraliza a imagem na metade esquerda (0.25 da tela total)
label_imagem.place(relx=0.25, rely=0.5, anchor="center")

# --- 2. CRIAR O PAINEL DE LOGIN (Lado Direito) ---
frame_login = ctk.CTkFrame(app, width=350, height=400, corner_radius=20)

# MUDANÇA AQUI: Centraliza o frame na metade direita (0.75 da tela total)
frame_login.place(relx=0.75, rely=0.5, anchor="center")

# Título dentro do Frame
titulo = ctk.CTkLabel(frame_login, text="LOGIN", font=("Arial", 30, "bold"))
titulo.pack(pady=(40, 20))

# Campo Usuário
campo_usuario = ctk.CTkEntry(frame_login, placeholder_text="Usuário", width=280, height=45)
campo_usuario.pack(pady=10)

# Campo Senha
campo_senha = ctk.CTkEntry(frame_login, placeholder_text="Senha", show="*", width=280, height=45)
campo_senha.pack(pady=10)

# Botão
botao = ctk.CTkButton(
    frame_login, 
    text="Entrar", 
    command=entrar, 
    fg_color="purple", 
    hover_color="#5e008a",
    width=200,
    height=45,
    corner_radius=10
)
botao.pack(pady=20)

# Mensagem de resultado
resultado = ctk.CTkLabel(frame_login, text="")
resultado.pack(pady=10)

app.mainloop()

