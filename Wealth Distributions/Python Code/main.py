import numpy as np
import system as s
import plot as pl


def main():
    N = 1000  # N es el número de agentes
    alpha = 1  # alpha es el dinero promedio
    beta = 1  # beta es la cantidad de bienes promedio
    T = 10 * N  # Tiempo de evolución
    w = 1
    a = np.full(N, alpha)
    b = np.full(N, beta)
    S = np.zeros(T)  # Entropía para cada tiempo
    M = 10
    bins = np.arange(0, 4, 0.1)
    E, Var = pl.histogram(N, alpha, beta, T, w, a, b, bins, S, M)
    k = E**2/Var
    theta = Var/E
    gammastr = "Gamma(" + str(k) + "," + str(theta)+")"
    pl.plot(bins, pl.gammadistribution(bins, k, theta), 4, 1.0, "Distribución de riqueza (f dist. gaussiana con sigma = 10.00)", "Riqueza",
            "Densidad de Probabilidad", "lightsalmon", gammastr)
    #s.sim(N, alpha, beta, T, w, a, b, bins, S)
    #pl.plot(range(T), S, T, 1.3, "Entropía de Shannon", "Iteración","Entropía [bits]", "limegreen", "Shannon's Entropy")


main()
