import urllib

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


def parse_requirements_file(path):
    with open(path) as f:
        for line in f.read().splitlines():
            line, *_ = line.split(" ")

            if line.startswith("-") or line.startswith("#"):
                continue

            if line.startswith("git+ssh://"):
                p = urllib.parse.urlparse(line)
                _, package_name = p.fragment.split("egg=")
                yield f"{package_name} @ {p.scheme}://{p.netloc}{p.path}"
            else:
                yield line


setuptools.setup(
    name="ai-agent",
    version="0.0.1",
    author="Caleb Carvalho",
    author_email="caleb.carvalho@gmail.com",
    description="Simple Agent with RAG Tool",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    include_package_data=True,
    package_dir={"": "src"},
    packages=setuptools.find_namespace_packages(where="src"),
    entry_points={
        "console_scripts": ["ai-agent = app.cli:cli"],
    },
    install_requires=list(parse_requirements_file("requirements.in")),
)
