import numpy as np
from .vector import VectorCoreset
from ..base.sampling import SamplingCoreset

class VectorSamplingCoreset(SamplingCoreset, VectorCoreset):

  def __init__(self, x, use_cached_xw=False):
    super().__init__(x=x, use_cached_xw=use_cached_xw, N=x.shape[0])

  def _xw_unscaled(self):
    return False

  def _compute_sampling_probabilities(self):
    if self.norm_sum > 0.:
      return self.norms.copy()
    else:
      return np.ones(self.N)

  def _weight_scaling(self):
    return self.norms


class VectorUniformSamplingCoreset(VectorSamplingCoreset):

  def _compute_sampling_probabilities(self):
    return np.ones(self.N)


