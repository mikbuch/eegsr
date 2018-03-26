import numpy as np
import pandas as pd
from sklearn.cross_decomposition import CCA

'''
This in an example of CCA.
'''

# How many samples to generate.
num_samples = 100

# Generate reference signal.
t = np.linspace(0, 1, num_samples)
Y = np.vstack([np.sin(2*np.pi*5*t), np.cos(2*np.pi*5*t)]).T
df_Y = pd.DataFrame(Y)
df_Y.plot(title='Reference signals')

# Add some noise to generate `acquired signal`.
noise = np.random.uniform(-0.5, 0.5, [num_samples, Y.shape[1]])
# Generated signal has sinusoidal shape.
X = Y[:, [0]] + noise
df_X = pd.DataFrame(X)
df_X.plot(title='Generated input signal (sin + noise)')

# Case #1: sinusoidal signal
cca = CCA(n_components=1)
cca.fit(X, Y)
U, V = cca.transform(X, Y)
# Alternatively:
# U, V = cca.fit_transform(X, Y)

corr = np.corrcoef(U.T, V.T)[0, 1]
print('CCA coef for sinusoidal data: %f.4' % corr)

# Case #2: random signal

# Some random samples.
X = np.random.rand(num_samples, Y.shape[1])
df_X = pd.DataFrame(X)
df_X.plot(title='Totally random')

cca = CCA(n_components=1)
cca.fit(X, Y)
U, V = cca.transform(X, Y)
# Alternatively:
# U, V = cca.fit_transform(X, Y)

corr = np.corrcoef(U.T, V.T)[0, 1]
print('CCA coef for random data: %f.4' % corr)
