from eegsr.dataset import fetch_example
from eegsr.control import Manager
from eegsr.decoding import CCA

'''
Take samples from source file, filters it and classifies.
'''

# Download example file and get it's location.
source_file = fetch_example('cca_ssvep_decoding')

cca = CCA(ref_signals={'type': 'ideal', 'harmonics': 1})

# If timecode set, the output will be written into file with current date.
manager = Manager(source_file=source_file, cls=cca, record_data=True,
                  output_file='timecode')
manager.run()
