from eegsr.dataset import fetch_example
from eegsr.preprocessing import FltRealTime
from eegsr.decoding import CCA
from eegsr.control import Manager

'''
Take samples from source file, filters it and classifies.
'''

# Download example file and get it's location.
source_file = fetch_example('cca_ssvep_decoding')

# Define filter object.
flt = FltRealTime(bandstop=(49, 51), bandpass=(1, 50))

# Define CCA object.
cca = CCA(ref_signals={'type': 'ideal', 'harmonics': 1})

# If timecode set, the output will be written into file with
# current date.
manager = Manager(filter=flt, cls=cca, source_file=source_file,
                  record_data=True, output_file='timecode')
manager.run()
