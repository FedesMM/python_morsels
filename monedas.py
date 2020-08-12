import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("historico monedas.csv")
data = data.dropna()
print(data.head())
agrupado = data.groupby(['Día']).mean()
print(agrupado)
print(agrupado.columns)
print(data[['EBORU_Dolar_Compra','EBORU_Dolar_Venta']].max())
#print(agrupado[['EBORU_Dolar_Compra','EBORU_Dolar_Venta']])

plt.plot(agrupado.index, agrupado['Dolar_Venta'], label='Venta Dolar', color= 'r')
plt.plot(agrupado.index, agrupado['Dolar_Compra'], label='Compra Dolar', color= 'b')
plt.suptitle('Precio Dolar\n Muesta 01/2017-07/2020')
plt.xlabel('Dia del mes')
plt.ylabel('Precio promedio a $')
plt.legend()
plt.show()

plt.plot(agrupado.index, agrupado['EBORU_Dolar_Venta'], label='Venta Dolar', color= 'r')
plt.plot(agrupado.index, agrupado['EBORU_Dolar_Compra'], label='Compra Dolar', color= 'b')
plt.suptitle('Precio Dolar EBROU\n Muesta 01/2017-07/2020')
plt.xlabel('Dia del mes')
plt.ylabel('Precio promedio a $')
plt.legend()
plt.show()