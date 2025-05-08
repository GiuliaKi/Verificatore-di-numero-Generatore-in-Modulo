import tkinter as tk


def is_generator(g, n, mode):
    residues = set()
    powers = []
    for k in range(1, n):
        if mode == "moltiplicativo":
            value = pow(g, k, n)
            powers.append(f"{g}^{k} mod {n} = {value}")
        else:  # additivo
            value = (g * k) % n
            powers.append(f"{g}×{k} mod {n} = {value}")
        residues.add(value)
    return residues, powers


def check_generator():
    try:
        n = int(entry_modulo.get())
        g = int(entry_generatore.get())
        mode = mode_var.get()

        if g <= 0 or g >= n:
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, f"Errore: Il generatore deve essere un numero tra 1 e {n - 1}\n")
            return

        residues, powers = is_generator(g, n, mode)

        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"{'Potenze' if mode == 'moltiplicativo' else 'Moltipli'} modulari calcolati:\n")
        for power in powers:
            output_text.insert(tk.END, power + "\n")

        final_font = ('Arial', 13, 'bold', 'underline')

        if len(residues) == n - 1:
            output_text.insert(tk.END, f"\n{g} è un generatore modulo {n}.", 'final_font')
        else:
            output_text.insert(tk.END, f"\n{g} NON è un generatore modulo {n}.", 'final_font')

    except ValueError:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Errore: Inserisci valori numerici validi.\n")



root = tk.Tk()
root.title("Verifica Generatore Modulo")
root.geometry("600x500")
root.config(bg="lightblue")

label_font = ('Arial', 12)

label_modulo = tk.Label(root, text="Inserisci il modulo (n):", font=label_font, bg="lightblue")
label_modulo.pack()
entry_modulo = tk.Entry(root, font=('Arial', 12))
entry_modulo.pack(pady=5)


label_generatore = tk.Label(root, text="Inserisci il generatore (g):", font=label_font, bg="lightblue")
label_generatore.pack()
entry_generatore = tk.Entry(root, font=('Arial', 12))
entry_generatore.pack(pady=5)


mode_var = tk.StringVar(value="moltiplicativo")
frame_radio = tk.Frame(root, bg="lightblue")
frame_radio.pack(pady=5)
tk.Label(frame_radio, text="Scegli il tipo di gruppo:", font=label_font, bg="lightblue").pack(side=tk.LEFT)
tk.Radiobutton(frame_radio, text="Moltiplicativo", variable=mode_var, value="moltiplicativo", bg="lightblue", font=label_font).pack(side=tk.LEFT)
tk.Radiobutton(frame_radio, text="Additivo", variable=mode_var, value="additivo", bg="lightblue", font=label_font).pack(side=tk.LEFT)


button_check = tk.Button(root, text="Verifica Generatore", command=check_generator, font=label_font, bg="lightgreen", relief="solid")
button_check.pack(pady=10)


frame = tk.Frame(root, bg="lightblue")
frame.pack()
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_text = tk.Text(frame, height=12, width=70, font=('Arial', 12), wrap=tk.WORD)
output_text.pack()
scrollbar.config(command=output_text.yview)
output_text.config(yscrollcommand=scrollbar.set)
output_text.tag_configure('final_font', font=('Arial', 13, 'bold', 'underline'))

root.mainloop()
