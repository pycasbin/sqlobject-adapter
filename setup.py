import setuptools

desc_file = "README.md"

with open(desc_file, "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="casbin_sqlobject_adapter",
    version="0.1.1",
    author="TechLee",
    author_email="techlee@qq.com",
    description="SQLObject Adapter for PyCasbin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pycasbin/sqlobject-adapter",
    keywords=["casbin", "SQLObject", "casbin-adapter", "rbac", "access control", "abac", "acl", "permission"],
    packages=setuptools.find_packages(),
    install_requires=['casbin>=0.8.4', 'SQLObject>=3.8.0'],
    python_requires=">=3.4",
    license="Apache 2.0",
    classifiers=[
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    data_files=[desc_file],
)