import sys
import subprocess
import os
import time

def show_message(title, message):
    # Fallback para print caso o tkinter não esteja disponível
    try:
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        if "erro" in title.lower():
            messagebox.showerror(title, message)
        else:
            messagebox.showinfo(title, message)
        root.destroy()
    except:
        print(f"{title}: {message}")

def check_python():
    if sys.version_info[0] < 3:
        show_message("Erro", "Python 3 não está instalado. Por favor, instale o Python 3 de python.org")
        os.system("start https://www.python.org/downloads/")
        sys.exit(1)

def install_pip():
    try:
        import pip
    except ImportError:
        show_message("Instalação", "Instalando pip...")
        try:
            subprocess.check_call([sys.executable, "-m", "ensurepip", "--default-pip"])
            show_message("Sucesso", "Pip instalado com sucesso!")
        except:
            show_message("Erro", "Falha ao instalar pip. Por favor, instale manualmente.")
            sys.exit(1)

def install_package(package):
    print(f"Instalando {package}...")
    try:
        if package == "customtkinter":
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])
        else:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar {package}: {str(e)}")
        return False

def check_and_install_dependencies():
    required_packages = ['customtkinter']
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"{package} já está instalado")
        except ImportError:
            print(f"{package} não encontrado. Tentando instalar...")
            if not install_package(package):
                show_message("Erro", f"Falha ao instalar {package}. O programa não pode continuar.")
                sys.exit(1)
            else:
                print(f"{package} instalado com sucesso!")

def main():
    try:
        print("Verificando requisitos...")
        check_python()
        install_pip()
        check_and_install_dependencies()
        
        print("Iniciando o programa principal...")
        time.sleep(1)  # Pequena pausa para garantir que tudo foi carregado
        
        from birimenu import BiriMenu
        app = BiriMenu()
        app.run()
        
    except Exception as e:
        error_msg = f"Erro ao iniciar o programa: {str(e)}"
        show_message("Erro", error_msg)
        print(error_msg)
        sys.exit(1)

if __name__ == "__main__":
    main() 