import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='pushover-notify',
     version='0.1.0',
     scripts=['pushover', 'pushover_exec'] ,
     author="Anton Suslov",
     author_email="anton_suslov@me.com",
     description="CLI interface for sending Pushover notifications",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/afakeman/pushover-notify",
     packages=setuptools.find_packages(),
     install_requires=[
         "requests",
     ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 3.7",
         "License :: Other/Propietary License",
         "Operating System :: OS Independent",
     ],
 )
