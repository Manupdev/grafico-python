from bokeh.plotting import figure, output_file, show
from csv import reader

def leer_csv():
    entrada = open('boca.csv','r')
    ganados = []
    ano=[]

    for linea in entrada:
        linea = linea.rstrip('\n')
        datos = linea.split(';')
        ano.append(datos[0])
        ganados.append(datos[1])
    crear_grafico(ano,ganados)

def crear_grafico(ano,ganados):
    output_file('grafico-boca.html')
    n=len(ano)
    fig1 = figure(x_range = ano, plot_height=500, plot_width=1300,title="Boca en la copa los ultimos 20 anios. Partidos Ganados")
    fig1.vbar(x=ano, top=ganados, width=0.5)
    fig1.y_range.start=0
    fig1.xaxis.major_label_orientation=1.2
    
    show(fig1)

        






if __name__ == '__main__':
    leer_csv()