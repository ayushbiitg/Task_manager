from setuptools import setup, find_packages

setup(
    name='tasks',
    version='0.1',  # Update with your project version
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django==4.2.8',
        'djangorestframework>=3.12,<4.0',
        'coverage>=5.5,<6.0',
    ],
    extras_require={
        'dev': [
            # Additional packages for development (if needed)
        ],
    },
    entry_points={
        'console_scripts': [
            # If your project has any console scripts, add them here
        ],
    },
)
