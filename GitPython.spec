# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           GitPython
Version:        0.2.0
Release:        0.5.beta1%{?dist}
Summary:        Python Git Library

Group:          Development/Languages
License:        BSD
URL:            http://pypi.python.org/pypi/GitPython/
Source0:        http://pypi.python.org/packages/source/G/GitPython/GitPython-%{version}-beta1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel python-setuptools
Requires:       /usr/bin/git
Patch0:         0001-Match-any-number-of-leading-spaces-in-config-values.patch

%description
GitPython is a python library used to interact with Git repositories.

GitPython provides object model access to your git repository. Once you have
created a repository object, you can traverse it to find parent commit(s),
trees, blobs, etc.

GitPython is a port of the grit library in Ruby created by Tom Preston-Werner
and Chris Wanstrath.


%prep
%setup -q -n %{name}-%{version}-beta1
%patch0 -p1


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README CHANGES LICENSE AUTHORS
# For noarch packages: sitelib
%{python_sitelib}/GitPython-%{version}_beta1-py*.egg-info
%{python_sitelib}/git


%changelog
* Mon Feb 14 2011 Jesse Keating <jkeating@redhat.com> - 0.2.0-0.5.beta1
- Fix parsing of config files

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-0.4.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 30 2010 Dennis Gilmore <dennis@ausil.us> - 0.2.0-0.3.beta1
- Require /usr/bin/git

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.2.0-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon May 24 2010 Devan Goodwin <dgoodwin@rm-rf.ca> - 0.2.0-0.1-beta1
- Updating for 0.2.0-beta1.

* Mon Jan 08 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.1.6-2
- Add python-setuptools to buildreq
- Explicit file list
- Use version macro in source url

* Wed Jan 06 2010 Jesse Keating <jkeating@redhat.com> - 0.1.6-1
- Initial Fedora package

