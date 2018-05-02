
class CCA(object):

    def __init__(ref_signals, fs, win_len, vis, verbose=True):

        self.ref_signals = {'type': 'ideal', 'harmonics': 1}
        self.fs = fs
        self.win_len = win_len
        self.vis = vis
        self.verbose = verbose


    def generate_ref(self, n_ch):

        m = self.win_len
        n = (self.ref_signals['harmonics']+1)*2

        self.ref = np.zeros((m, n))

        t = np.linspace(0, 1, num_samples)

        for i in range(n):
            if i % 2 == 0:
                self.ref[i] = np.array([np.sin(2*np.pi*i*self.hz)
                                        for i in t])
            else


        self.cos = np.array([np.cos(2*np.pi*i*self.hz) for i in t])

        self.sin_2 = np.array([np.sin(2*np.pi*i*self.hz*2) for i in t])
        self.cos_2 = np.array([np.cos(2*np.pi*i*self.hz*2) for i in t])

        self.reference[:, 0] = self.sin
        self.reference[:, 1] = self.cos
        self.reference[:, 2] = self.sin_2
        self.reference[:, 3] = self.cos_2
