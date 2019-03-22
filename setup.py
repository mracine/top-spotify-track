from setuptools import setup

setup(
        name='top-spotify-track',
        packages=['top-spotify-track'],
        include_package_data=True,
        install_requires=[
            'flask',
            'spotipy',
            ],
        test_suite="tests",
        )

