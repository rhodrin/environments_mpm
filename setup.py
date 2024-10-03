from setuptools import setup

setup(
    name='envtest',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description="Playing with virtual environments.",
    long_description="Playing with virtual environments.",
    author="Imperial College London",
    author_email='rhodri.nelson@imperial.ac.uk',
    packages=['envtest'],
)


