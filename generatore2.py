import tkinter as tk


def is_generator(g, n):
    residues = set()
    powers = []
    for k in range(1, n):
        value = pow(g, k, n)
        residues.add(value)
        powers.append(f"{g}^{k} mod {n} = {value}")
    return residues, powers


def check_generator():
    try:
        n = int(entry_modulo.get())
        g = int(entry_generatore.get())

        if g <= 0 or g >= n:
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, f"Errore: Il generatore deve essere un numero tra 1 e {n - 1}\n")
            return

        residues, powers = is_generator(g, n)

        output_text.delete(1.0, tk.END)

        # Mostra tutte le potenze calcolate
        output_text.insert(tk.END, "Potenze modulari calcolate:\n")
        for power in powers:
            output_text.insert(tk.END, power + "\n")

        # Font per il testo finale (grassetto e sottolineato)
        final_font = ('Arial', 12, 'bold', 'underline')

        # Verifica se è un generatore e applica il font modificato
        if len(residues) == n - 1:
            output_text.insert(tk.END, f"\n{g} è un generatore modulo {n}.", 'final_font')
        else:
            output_text.insert(tk.END, f"\n{g} NON è un generatore modulo {n}.", 'final_font')

    except ValueError:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Errore: Inserisci valori numerici validi.\n")


# Crea la finestra principale
root = tk.Tk()
root.title("Verifica Generatore Modulo")
root.geometry("600x400")  # Imposta la dimensione della finestra

# Imposta il colore di sfondo della finestra principale
root.config(bg="lightblue")  # Colore di sfondo della finestra principale

# Imposta il font personalizzato per le etichette
label_font = ('Arial', 12)

# Crea gli elementi dell'interfaccia
label_modulo = tk.Label(root, text="Inserisci il modulo (n):", font=label_font, bg="lightblue")
label_modulo.pack()

entry_modulo = tk.Entry(root, font=('Arial', 12))  # Font della casella di testo
entry_modulo.pack(pady=5)

label_generatore = tk.Label(root, text="Inserisci il generatore (g):", font=label_font, bg="lightblue")
label_generatore.pack()

entry_generatore = tk.Entry(root, font=('Arial', 12))  # Font della casella di testo
entry_generatore.pack(pady=5)

# Cambia il colore del bottone
button_check = tk.Button(root, text="Verifica Generatore", command=check_generator, font=label_font, bg="lightgreen", relief="solid")
button_check.pack(pady=10)

# Crea un frame per la TextBox e la Scrollbar
frame = tk.Frame(root, bg="lightblue")
frame.pack()

# Aggiungi una barra di scorrimento verticale
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Crea la TextBox per i risultati con un font personalizzato
output_text = tk.Text(frame, height=10, width=70, font=('Arial', 12), wrap=tk.WORD)
output_text.pack()

# Associa la scrollbar alla TextBox
scrollbar.config(command=output_text.yview)
output_text.config(yscrollcommand=scrollbar.set)

# Aggiungi lo stile personalizzato per la parte finale (grassetto e sottolineato)
output_text.tag_configure('final_font', font=('Arial', 13, 'bold', 'underline'))

# Avvia l'interfaccia grafica
root.mainloop()
