import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

if __name__ == "__main__":
    setuptools.setup(
        name="SMNCopyNumberCaller",
        version="0.0.0.1",
        author="ILMN",
        author_email="na@na.gov",
        description="Just making this installable via conda",
        long_description="see description",
        long_description_content_type="text/markdown",
        url="thub.com/iamh2o/SMNCopyNumberCaller",
        project_urls={
            "Bug Tracker": "https://github.com/iamh2o/SMNCopyNumberCaller",
        },
        packages=['SMNCopyNumberCaller', 'SMNCopyNumberCaller.caller', 'SMNCopyNumberCaller.depth_calling','SMNCopyNumberCaller.charts'],
        package_data={'SMNCopyNumberCaller': ['SMNCopyNumberCaller/data/*']},
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: PolyForm Strict License 1.0.0",
            "Operating System :: OS Independent",
        ],
        setup_requires=['pytest-runner'],
        tests_require=['pytest'],
        package_dir={"SMNCopyNumberCaller": "SMNCopyNumberCaller"}, #packages=setuptools.find_packages(where="SMNCopyNumberCaller"),
        scripts=[
            "bin/smn_caller.py",
	    "bin/smn_charts.py"
        ],
        python_requires=">=3.7",
        install_requires=[
            "reportlab",
            "numpy >=1.16",
            "scipy >=1.2",
            "pysam >=0.15.3",
            "statsmodels >=0.9",
        ],
        includde_package_data=True,
        zip_safe=False,
        
    )
    
