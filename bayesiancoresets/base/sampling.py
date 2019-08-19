import numpy as np
from .coreset import Coreset


#TODO somehow allow sparsity here so we don't have to store N cts/ps/etc
class SamplingCoreset(Coreset):

  def __init__(self, sampling_probabilities=None, **kw):
    super().__init__(**kw)
    if sampling_probabilities is None:
      self.ps = self._compute_sampling_probabilities()
    else:
      self.ps = sampling_probabilities
    if np.any(self.ps < 0.):
      raise ValueError(self.alg_name+'.__init__(): sampling probabilities must be all nonnegative')
    self.ps /= self.ps.sum()
    self.cts = np.zeros(self.N)
    
  def reset(self):
    super().reset()
    self.cts = np.zeros(self.N)
    
  def _build(self, sz, itrs):
    self.cts += np.random.multinomial(min(itrs, sz - self.cts.sum()), self.ps)
    active = np.where(self.cts > 0)[0]
    self._overwrite(active, self.cts[active]/self.ps[active]/sz)

  #defaults to uniform sampling
  def _compute_sampling_probabilities(self):
    raise NotImplementedError


