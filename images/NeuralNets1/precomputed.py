
class SquareSawtoothPrecomputed(Dataset):
    def __init__(self, n_samples, pmin, pmax, sr, N, do_fft=False):
        """
        Fix frequencies, augment on amplitude and phase
        
        Parameters
        ----------
        n_samples: int
            Number of samples
        pmin: int
            Minimum note number
        pmax: int
            Maximum note number
        sr: int
            Sample rate
        N: int
            Number of samples per example
        """
        X = torch.zeros((n_samples, N))
        labels = torch.zeros(n_samples)
        for i in range(n_samples):
            p = np.random.randint(p1, p2+1)
            f = 440*2**(p/12)
            phi = 2*np.pi*np.random.rand()
            A = np.random.rand()
            label = 0
            if np.random.rand() < 0.5:
                x = get_square(A, f, phi, sr, N)
            else:
                label = 1
                x = get_sawtooth(A, f, phi, sr, N)
            X[i, :] = torch.from_numpy(np.array(x, dtype=np.float32))
            if do_fft:
                X[i, :] = np.abs(torch.fft.fft(X[i, :]))
        self.X = X
        self.labels = labels
        print("Finished precomputing {} examples".format(n_samples))
    
    def __len__(self):
        return self.X.shape[0]
    
    def __getitem__(self, idx):
        return self.X[idx, :], self.labels[idx]
