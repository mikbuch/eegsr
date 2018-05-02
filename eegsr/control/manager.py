


class Manager(object):

    def __init__(self, filter, classifier, source_file, record_data,
                 oputput_file):

        self.filter = filter
        self.classifier = classifier
        self.source_file = source_file
        self.record_data = record_data
        self.output_file = output_file

        #TODO make simulator return num of channels
        self.board = bci_sim.OpenBCISimulator(self.source_file)
        # Tell classifier how many channels there are.
        self.classifier.generate_ref(self.board.getNbEEGChannels())


    def run(self):

        def handle_sample(sample):

            self.filter.filter_data(sample.channel_data)

            self.classifier.classify(self.filter.sample)

        # Board connection #
        self.board.start_streaming(handle_sample)
