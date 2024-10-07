from setuptools import setup, find_packages

setup(
    name='envtest',
    use_scm_version={
        "write_to": "envtest/_version.py",  # Optional: writes the version to a file
        "version_scheme": "no-guess-dev",   # Version scheme that doesn't require tags
        "local_scheme": "node-and-date",    # Use commit hash and date for local version
    },
    setup_requires=['setuptools_scm'],
    description="Playing with virtual environments.",
    long_description="Playing with virtual environments.",
    author="Imperial College London",
    author_email='rhodri.nelson@imperial.ac.uk',
    packages=find_packages(),
)
