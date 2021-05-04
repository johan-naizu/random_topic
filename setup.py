import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="random-topics",
    version="0.1.0",
    author="Johan Naizu",
    author_email="johan@naizu.in",
    description="module to fetch random topics for conversation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johan-naizu/random-topics",
    project_urls={
        "Bug Tracker": "https://github.com/johan-naizu/random-topics/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
