import setuptools

with open("ReadMe.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='esa',
    version='0.6.3',
    description='Easy SimAuto (ESA): An easy-to-use Python connector to '
                'PowerWorld Simulator Automation Server (SimAuto).',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Zeyu Mao, Brandon Thayer, Yijing Liu',
    author_email='zeyumao2@tamu.edu, blthayer@tamu.edu, yiji21@tamu.edu',
    url='https://github.com/mzy2240/ESA',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Win32 (MS Windows)",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Topic :: Education",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",

    ],
    keywords=['Python', 'PowerWorld', 'PowerWorld Simulator', 'Simulator',
              'PowerWorld Simulation Automation Server', 'SimAuto',
              'Automation', 'Power Systems', 'Electric Power', 'Power',
              'Easy SimAuto', 'ESA', 'Smart Grid', 'Numpy', 'Pandas'],
    install_requires=['pandas >= 0.24', 'numpy', 'pywin32', 'pypiwin32'],
    python_requires='>=3.5',
    license='MIT',
    zip_safe=False
)
