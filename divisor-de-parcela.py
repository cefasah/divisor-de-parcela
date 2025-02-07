import logging
import tkinter as tk
from tkinter import messagebox

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calcular_emprestimo(valor: float, parcelas: int, taxa_juros: float) -> tuple:
    """Calcula o valor total do empréstimo e o valor de cada parcela."""
    try:
        valor_total = valor * ((1 + taxa_juros) ** parcelas)
        valor_parcela = valor_total / parcelas
        return round(valor_total, 2), round(valor_parcela, 2)
    except Exception as e:
        logging.error(f"Erro ao calcular empréstimo: {e}")
        raise

def definir_taxa_juros(tipo: str, score_credito: int) -> float:
    """Define a taxa de juros com base no tipo de empréstimo e no score de crédito."""
    taxas_base = {"pessoal": 0.02, "consignado": 0.01}
    taxa = taxas_base.get(tipo, None)
    
    if taxa is None:
        raise ValueError("Tipo de empréstimo inválido.")
    
    # Ajuste baseado no score de crédito
    if score_credito >= 800:
        taxa *= 0.8  # 20% de desconto para ótimo score
    elif score_credito < 500:
        taxa *= 1.2  # 20% de aumento para baixo score
    
    return round(taxa, 5)

def calcular_e_exibir():
    try:
        valor = float(entry_valor.get())
        parcelas = int(entry_parcelas.get())
        tipo_emprestimo = entry_tipo.get().strip().lower()
        score_credito = int(entry_score.get())

        if not (1 <= parcelas <= 60):
            raise ValueError("O número de parcelas deve estar entre 1 e 60.")
        if not (300 <= score_credito <= 850):
            raise ValueError("Score de crédito deve estar entre 300 e 850.")

        taxa_juros = definir_taxa_juros(tipo_emprestimo, score_credito)
        valor_total, valor_parcela = calcular_emprestimo(valor, parcelas, taxa_juros)

        resultado_text.set(f"\nValor total a ser pago: R${valor_total:,.2f}\nValor de cada parcela: R${valor_parcela:,.2f}\n")
        logging.info("Empréstimo calculado com sucesso!")
    except ValueError as ve:
        messagebox.showerror("Erro", f"Entrada inválida: {ve}")
    except Exception as e:
        logging.critical(f"Erro inesperado: {e}")
        messagebox.showerror("Erro", "Ocorreu um erro inesperado. Tente novamente mais tarde.")

# Criando a interface gráfica
root = tk.Tk()
root.title("Simulador de Empréstimos")
root.geometry("550x450")
root.configure(bg="#2C3E50")

frame = tk.Frame(root, padx=20, pady=20, bg="#ECF0F1", relief=tk.RIDGE, borderwidth=3)
frame.pack(pady=20)

tk.Label(frame, text="Simulador de Empréstimos", font=("Arial", 18, "bold"), bg="#ECF0F1", fg="#2C3E50").pack(pady=10)

tk.Label(frame, text="Valor do Empréstimo (R$):", bg="#ECF0F1", font=("Arial", 12)).pack()
entry_valor = tk.Entry(frame, width=30, font=("Arial", 12))
entry_valor.pack()

tk.Label(frame, text="Número de Parcelas (1-60):", bg="#ECF0F1", font=("Arial", 12)).pack()
entry_parcelas = tk.Entry(frame, width=30, font=("Arial", 12))
entry_parcelas.pack()

tk.Label(frame, text="Tipo de Empréstimo (pessoal/consignado):", bg="#ECF0F1", font=("Arial", 12)).pack()
entry_tipo = tk.Entry(frame, width=30, font=("Arial", 12))
entry_tipo.pack()

tk.Label(frame, text="Score de Crédito (300-850):", bg="#ECF0F1", font=("Arial", 12)).pack()
entry_score = tk.Entry(frame, width=30, font=("Arial", 12))
entry_score.pack()

# Botão para calcular
btn_calcular = tk.Button(frame, text="Calcular", command=calcular_e_exibir, bg="#27AE60", fg="white", font=("Arial", 14, "bold"), width=20)
btn_calcular.pack(pady=15)

# Área de resultado
resultado_text = tk.StringVar()
resultado_label = tk.Label(frame, textvariable=resultado_text, bg="#ECF0F1", font=("Arial", 14, "bold"), fg="#C0392B")
resultado_label.pack()

# Rodando a interface gráfica
root.mainloop()

            taxa_juros = 0.02  
        elif tipo_emprestimo == "consignado":
            taxa_juros = 0.01  
        else:
            print("Tipo de empréstimo inválido.")
            taxa_juros = None

        if taxa_juros is not None:
            valor_total, valor_parcela = calcular_emprestimo(valor, parcelas, taxa_juros)
            exibir_detalhes_emprestimo(valor, parcelas, valor_total, valor_parcela, taxa_juros)

except ValueError:
    print("Entrada inválida. Por favor, insira apenas números.")
