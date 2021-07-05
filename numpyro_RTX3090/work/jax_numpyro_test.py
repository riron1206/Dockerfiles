# jax test
# https://zenn.dev/asei/articles/ee0525e452fdb3

## Prevent GPU/TPU warning.
#import jax; jax.config.update('jax_platform_name', 'cpu')

# ====================================
# NumPy 互換の行列演算
# ====================================
import jax.numpy as jnp
import numpy as np
size = 10
x = np.random.normal(size=(size, size)).astype(np.float32)
jnp.dot(x, x.T).block_until_ready()

from jax import random
key = random.PRNGKey(0)
size = 3000
x = random.normal(key, (size, size), dtype=jnp.float32)
jnp.dot(x, x.T).block_until_ready()  # runs on the GPU

# ====================================
# 自動微分
# ====================================
import jax.numpy as jnp
from jax import grad
def sum_logistic(x):
    return jnp.sum(1.0 / (1.0 + jnp.exp(-x)))
key = random.PRNGKey(0)
x_small = jnp.arange(3.)
derivative_fn = grad(sum_logistic)  # 導関数（1回微分）の値計算
print(derivative_fn(x_small))
# [0.25       0.19661197 0.10499357]
print(grad(grad(grad(sum_logistic)))(1.0))  # grad を重ねることで高階微分（3回微分）の値計算
# -0.035325598

# ====================================
# CNN 構築
# ====================================
import jax.numpy as jnp
from jax import random
from jax.experimental import stax
from jax.experimental.stax import Conv, Dense, MaxPool, Relu, Flatten, LogSoftmax
# Use stax to set up network initialization and evaluation functions
net_init, net_apply = stax.serial(
    Conv(32, (3, 3), padding='SAME'), Relu,
    Conv(64, (3, 3), padding='SAME'), Relu,
    MaxPool((2, 2)), Flatten,
    Dense(128), Relu,
    Dense(10), LogSoftmax,
)


# GPUだとMCMC遅いのでcpu使う
import numpyro
numpyro.set_platform("cpu")

# ====================================
# 公式github の numpyro sample code
# https://github.com/pyro-ppl/numpyro
# ====================================
import numpy as np
J = 8
y = np.array([28.0, 8.0, -3.0, 7.0, -1.0, 1.0, 18.0, 12.0])
sigma = np.array([15.0, 10.0, 16.0, 11.0, 9.0, 11.0, 10.0, 18.0])

# 観測データが平均と標準偏差の正規分布から生成されると仮定して、調査の階層モデルを構築
import numpyro
import numpyro.distributions as dist
# Eight Schools example
def eight_schools(J, sigma, y=None):
    mu = numpyro.sample('mu', dist.Normal(0, 5))
    tau = numpyro.sample('tau', dist.HalfCauchy(5))
    with numpyro.plate('J', J):
        theta = numpyro.sample('theta', dist.Normal(mu, tau))
        numpyro.sample('obs', dist.Normal(theta, sigma), obs=y)

# MCMCを実行
from jax import random
from numpyro.infer import MCMC, NUTS
nuts_kernel = NUTS(eight_schools)
mcmc = MCMC(nuts_kernel, num_warmup=500, num_samples=1000)
rng_key = random.PRNGKey(0)
mcmc.run(rng_key, J, sigma, y=y, extra_fields=('potential_energy',))

# 予想される対数同時密度を計算
mcmc.print_summary()
pe = mcmc.get_extra_fields()['potential_energy']
print('Expected log joint density: {:.2f}'.format(np.mean(-pe)))

# theta_base基本Normal(0, 1)分布のサンプルを生成してHMCを実行
from numpyro.infer.reparam import TransformReparam
# Eight Schools example - Non-centered Reparametrization
def eight_schools_noncentered(J, sigma, y=None):
    mu = numpyro.sample('mu', dist.Normal(0, 5))
    tau = numpyro.sample('tau', dist.HalfCauchy(5))
    with numpyro.plate('J', J):
        with numpyro.handlers.reparam(config={'theta': TransformReparam()}):
            theta = numpyro.sample(
                'theta',
                dist.TransformedDistribution(dist.Normal(0., 1.),
                                             dist.transforms.AffineTransform(mu, tau)))
        numpyro.sample('obs', dist.Normal(theta, sigma), obs=y)
nuts_kernel = NUTS(eight_schools_noncentered)
mcmc = MCMC(nuts_kernel, num_warmup=500, num_samples=1000)
rng_key = random.PRNGKey(0)
mcmc.run(rng_key, J, sigma, y=y, extra_fields=('potential_energy',))
mcmc.print_summary(exclude_deterministic=False)  # doctest: +SKIP
pe = mcmc.get_extra_fields()['potential_energy']
print('Expected log joint density: {:.2f}'.format(np.mean(-pe)))  # doctest: +SKIP

# 予測を生成
from numpyro.infer import Predictive
# New School
def new_school():
    mu = numpyro.sample('mu', dist.Normal(0, 5))
    tau = numpyro.sample('tau', dist.HalfCauchy(5))
    return numpyro.sample('obs', dist.Normal(mu, tau))
predictive = Predictive(new_school, mcmc.get_samples())
samples_predictive = predictive(random.PRNGKey(1))
print(np.mean(samples_predictive['obs']))  # doctest: +SKIP

