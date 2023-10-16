import pandas as pd
import matplotlib.pyplot as plt

def plot_graphic_points(value):
    try:
        df = pd.read_csv(value)

        if 'total' not in df.columns:

            print("O arquiv a coluna 'total'.")
            return

        df['total'] = pd.to_numeric(df['total'], errors='coerce')

        df = df.dropna(subset=['total'])

        plt.scatter(range(1, len(df) + 1), df['total'])
        plt.xlabel('Índice')
        plt.ylabel('Valor Total')
        plt.title('Gráfico de Pontos da Coluna "total"')
        plt.show()

    except FileNotFoundError:
        print(f"'{value}' não encontrado.")
    except Exception as e:
        print(f"erro: {str(e)}")

plot_graphic_points("movies.csv")
