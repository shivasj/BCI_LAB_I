print('\n\t============ Machine learning - Features ============\n') 

# Example to use the obtained data
    # Plot amplitude in function of frequencies

def PlotPowerSit(power_sit):
    for i in range(3):
        for j in range(19):
            for k in range(0,10241,1000):
                # power.data[j][k][l]: j:n_channels, k:n_freqs, l:n_times
                plt.plot(frequencies[j],power_sit.data[i][j][k],'bx-')
    plt.title('Demonsration of features')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    #plt.ylim([0,1e-8])
    plt.show()

plot_power_sit = mp.Process(target=PlotPowerSit,args=[power_sit])
plot_power_sit.start()