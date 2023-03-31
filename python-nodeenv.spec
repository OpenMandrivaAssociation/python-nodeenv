%global pypi_name nodeenv

Name:           python-%{pypi_name}
Version:        1.7.0
Release:        2
Summary:        Node.js virtual environment builder
Group:          Development/Python
License:        BSD
URL:            https://github.com/ekalinin/nodeenv
Source0:        https://files.pythonhosted.org/packages/source/n/nodeenv/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Node.js virtual environment nodeenv (node.js virtual environment) is a tool to
create isolated node.js environments.It creates an environment that has its own
installation directories, that doesn't share libraries with other node.js
virtual environments.Also the new environment can be integrated with the
environment which was built by virtualenv_ (python).If you use nodeenv feel
free to add...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst README.ru.rst
%{_bindir}/nodeenv
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
