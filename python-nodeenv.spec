%global pypi_name nodeenv

Name:           python-%{pypi_name}
Version:        1.9.1
Release:        1
Summary:        Node.js virtual environment builder
Group:          Development/Python
License:        BSD
URL:            https://github.com/ekalinin/nodeenv
Source0:        https://files.pythonhosted.org/packages/source/n/nodeenv/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildSystem:	python
BuildRequires:  python%{pyver}dist(setuptools)

# Called through subprocess.Popen in nodeenv.py
Requires:	which

%description
Node.js virtual environment nodeenv (node.js virtual environment) is a tool to
create isolated node.js environments.It creates an environment that has its own
installation directories, that doesn't share libraries with other node.js
virtual environments.Also the new environment can be integrated with the
environment which was built by virtualenv_ (python).If you use nodeenv feel
free to add...

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst README.ru.rst
%{_bindir}/nodeenv
%{python_sitelib}/__pycache__/*
%{python_sitelib}/%{pypi_name}.py
%{python_sitelib}/%{pypi_name}-%{version}.dist-info
