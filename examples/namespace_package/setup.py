from setuptools import setup, find_namespace_packages
from setuptools_rust import Binding, RustExtension


setup(
    name='namespace_package',
    version="0.1.0",
    packages=find_namespace_packages(include=['namespace_package.*']),
    zip_safe=False,
    rust_extensions=[RustExtension("namespace_package.bar", path="Cargo.toml", binding=Binding.PyO3, debug=False)],
)
