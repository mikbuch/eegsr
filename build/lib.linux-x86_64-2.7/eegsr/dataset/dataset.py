import urllib
import os


def fetch_example(signal_type, local_fname=None, verbose=1):
    """ Get an example file from the internet

    Download file to default or specified location and return it's pathself.

    Parameters
    ----------
    signal_type : str
        Specify one of the signal types to be downloaded, available options:
        'cca_ssvep_decoding'.
    local_fname : str | None
        You may specify where to download the files. If no path is specified
        (None, dedault value) the default dir is ~/eeg_data/eegsr.
    """

    if signal_type == 'cca_ssvep_decoding':
        url = ''

    if local_fname is None:
        local_fname = '%s%s.csv' % (os.environ['HOME'], signal_type)

    #TODO mkdir if not existing (eeg_data/eegsr)
    urllib.retrieveurl(url, local_fname)

    if verbose >= 1:
        print('Signal `%s` downloaded to: %s' % (signal_type, local_fname))

    return local_fname
