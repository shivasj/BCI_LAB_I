print('\n\t============ Events ============\n')

# Extract events
events = mne.find_events(raw, 
                         stim_channel='STI 014')
print(events)
print('\n')

# Read and write events to avoid recalculating
    # mne.write_events('events.fif', events)
    # events = mne.read_events('events.fif')

# Plot raw EEG data with event markers
if FLAG_MP:
    def PlotRawData(raw, events):
        fig_rawdata = raw.plot(events=events,
                            event_color= 'r', 
                            show_options='True', 
                            title='Raw data')
        plt.show()

    print 'plot_rawdata: Creating new process'
    plot_rawdata = mp.Process(target=PlotRawData,args=[raw,events])
    print 'plot_rawdata: Starting new process'
    plot_rawdata.start()
    print 'plot_rawdata: Process created\n'

elif FLAG_PLOT:
    fig_rawdata = raw.plot(events=events,
                           event_color= 'r', 
                           show_options='True', 
                           title='Raw data')
    plt.show()



event_id = {'INIT': 65280 + 255, # Offset required since MNE 0.9 update
	    'CUE': 65280 + 254, 
	    'BLANK': 65280 + 252, 
	    'STAND_READY': 65280 + 241, 
	    'STAND_GO': 65280 + 240,
	    'SIT_READY': 65280 + 239,
	    'SIT_GO': 65280 + 238}
#'WALK_READY':237
#'WALK_GO':236

#event_id = {'INIT': 65535,
            #'CUE': 65534, 
            #'BLANK': 65520, 
            #'STAND_READY': 65521, 
            #'STAND_GO': 65532,
            #'SIT_READY': 65534,
            #'SIT_GO': }
#Events id: [65518 65519 65520 65521 65532 65534 65535]

# Event times
print 'EVENTS TIMES:'
event_sit_go_time = []
event_stand_go_time = []
event_sit_go_time_total = 0
event_stand_go_time_total = 0
for i in range(len(events[:,0])):
    if events[i,2] == 65280 + 238:
        print i, 'Event SIT_GO from time', events[i,0]/sampling_time
        event_sit_go_time.append([events[i,0]/sampling_time,events[i+1,0]/sampling_time])
        event_sit_go_time_total += (events[i+1,0] - events[i,0])/sampling_time
    elif events[i,2] == 65280 + 240:
        print i, 'Event STAND_GO at time', events[i,0]/sampling_time
        event_stand_go_time.append([events[i,0]/sampling_time,events[i+1,0]/sampling_time])
        event_stand_go_time_total += (events[i+1,0] - events[i,0])/sampling_time

print 'Total Sitting time:', event_sit_go_time_total, 'seconds'
print 'Total Standing time:', event_stand_go_time_total, 'seconds'
print '\n'

# Plot events
if FLAG_MP:
    def PlotEvents(raw, events, event_id):
        fig_events = mne.viz.plot_events(events,
                                        raw.info['sfreq'],
                                        raw.first_samp,
                                        event_id=event_id,
                                        show=False)
        plt.title('Events')
        plt.show()

    print 'plot_events: Creating new process'
    plot_events = mp.Process(target=PlotEvents,args=[raw, events, event_id])
    print 'plot_events: Starting new process'
    plot_events.start()
    print 'plot_events: Process created\n'
elif FLAG_PLOT:
    fig_events = mne.viz.plot_events(events,
                                        raw.info['sfreq'],
                                        raw.first_samp,
                                        event_id=event_id,
                                        show=False)
    plt.title('Events')
    plt.show()


