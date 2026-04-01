%define module nodeenv

Name:		python-nodenev
Summary:	Node.js virtual environment builder
Version:	1.10.0
Release:	1
License:	BSD-3-Clause
Group:  	Development/Python
URL:		https://github.com/ekalinin/nodeenv
Source0:	https://files.pythonhosted.org/packages/source/n/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
Requires:	python%{pyver}dist(setuptools)
# Called through subprocess.Popen in nodeenv.py
Requires:	which

%description
Node.js virtual environment nodeenv (node.js virtual environment) is a tool to
create isolated node.js environments.It creates an environment that has its own
installation directories, that doesn't share libraries with other node.js
virtual environments.Also the new environment can be integrated with the
environment which was built by virtualenv_ (python).If you use nodeenv feel
free to add...

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%doc README.rst README.ru.rst
%license LICENSE
%{_bindir}/%{module}
%{python_sitelib}/__pycache__/%{module}*
%{python_sitelib}/%{module}.py
%{python_sitelib}/%{module}-%{version}.dist-info
