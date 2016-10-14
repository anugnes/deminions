from distutils.core import setup

setup(
    name='deminions',
    version='1.0.0',
    packages=['check_cmile.Libraries'],
    url='',
    license='Proprietary',
    author='Alberto Nugnes',
    author_email='nugnes.alberto@gmail.com',
    description='Minion that fetches a URL and sends an email via Gmail if the return code is not 200'
)
