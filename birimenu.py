import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk

class BiriMenu:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Biri Menu - Five M Hack")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Configuração do tema escuro
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        # Frame principal
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Título
        self.title_label = ctk.CTkLabel(
            self.main_frame, 
            text="Biri Menu", 
            font=("Roboto", 24, "bold")
        )
        self.title_label.pack(pady=10)
        
        # Botões de funcionalidades
        self.godmode_var = tk.BooleanVar()
        self.godmode_switch = ctk.CTkSwitch(
            self.main_frame,
            text="God Mode",
            variable=self.godmode_var,
            command=self.toggle_godmode
        )
        self.godmode_switch.pack(pady=10)
        
        self.aimbot_var = tk.BooleanVar()
        self.aimbot_switch = ctk.CTkSwitch(
            self.main_frame,
            text="Aimbot",
            variable=self.aimbot_var,
            command=self.toggle_aimbot
        )
        self.aimbot_switch.pack(pady=10)
        
        self.esp_var = tk.BooleanVar()
        self.esp_switch = ctk.CTkSwitch(
            self.main_frame,
            text="ESP (Wallhack)",
            variable=self.esp_var,
            command=self.toggle_esp
        )
        self.esp_switch.pack(pady=10)
        
        # Slider para velocidade
        self.speed_label = ctk.CTkLabel(
            self.main_frame,
            text="Velocidade do Personagem:"
        )
        self.speed_label.pack(pady=5)
        
        self.speed_slider = ctk.CTkSlider(
            self.main_frame,
            from_=1,
            to=10,
            command=self.change_speed
        )
        self.speed_slider.pack(pady=10)
        
        # Botão para teleporte
        self.teleport_button = ctk.CTkButton(
            self.main_frame,
            text="Teleportar para Waypoint",
            command=self.teleport
        )
        self.teleport_button.pack(pady=10)
        
        # Botão para spawnar veículo
        self.vehicle_entry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="Nome do veículo"
        )
        self.vehicle_entry.pack(pady=10)
        
        self.spawn_vehicle_button = ctk.CTkButton(
            self.main_frame,
            text="Spawnar Veículo",
            command=self.spawn_vehicle
        )
        self.spawn_vehicle_button.pack(pady=10)
        
    def toggle_godmode(self):
        if self.godmode_var.get():
            messagebox.showinfo("God Mode", "God Mode ativado!")
        else:
            messagebox.showinfo("God Mode", "God Mode desativado!")
            
    def toggle_aimbot(self):
        if self.aimbot_var.get():
            messagebox.showinfo("Aimbot", "Aimbot ativado!")
        else:
            messagebox.showinfo("Aimbot", "Aimbot desativado!")
            
    def toggle_esp(self):
        if self.esp_var.get():
            messagebox.showinfo("ESP", "ESP ativado!")
        else:
            messagebox.showinfo("ESP", "ESP desativado!")
            
    def change_speed(self, value):
        print(f"Velocidade alterada para: {value}")
        
    def teleport(self):
        messagebox.showinfo("Teleporte", "Teleportando para o waypoint...")
        
    def spawn_vehicle(self):
        vehicle_name = self.vehicle_entry.get()
        if vehicle_name:
            messagebox.showinfo("Veículo", f"Spawning veículo: {vehicle_name}")
        else:
            messagebox.showerror("Erro", "Por favor, insira o nome do veículo!")
            
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    try:
        app = BiriMenu()
        app.run()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao executar o programa: {str(e)}")
