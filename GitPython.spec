# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           GitPython
Version:        0.3.2
Release:        0.6.RC1%{?dist}
Summary:        Python Git Library

Group:          Development/Languages
License:        BSD
URL:            http://pypi.python.org/pypi/GitPython/
# http://pypi.python.org/packages/source/G/GitPython/GitPython-0.3.2.RC1.tar.gz#md5=849082fe29adc653a3621465213cab96
Source0:        http://pypi.python.org/packages/source/G/GitPython/GitPython-0.3.2.RC1.tar.gz
Patch1:         0001-GPG-signature-support-on-commit-object.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel python-setuptools
Requires:       git
Requires:       python-gitdb

%description
GitPython is a python library used to interact with Git repositories.

GitPython provides object model access to your git repository. Once you have
created a repository object, you can traverse it to find parent commit(s),
trees, blobs, etc.

GitPython is a port of the grit library in Ruby created by Tom Preston-Werner
and Chris Wanstrath.


%prep
%setup -q -n %{name}-%{version}.RC1
%patch1 -p1

%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE AUTHORS
# For noarch packages: sitelib
%{python_sitelib}/GitPython-%{version}.RC1-py*.egg-info
%{python_sitelib}/git


%changelog
* Sat Dec 07 2013 Dennis Gilmore <dennis@ausil.us> - 0.3.2-0.6-RC1
- apply patch from Igor Gnatenko for bz#1010706

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-0.5.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-0.4.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-0.3.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-0.2.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 23 2011 Jesse Keating <jkeating@redhat.com> - 0.3.2-0.1.RC1
- Update to 0.3.2 RC1

* Fri May 27 2011 Jesse Keating <jkeating@redhat.com> - 0.2.0-0.6.beta1
- Patches for indented parts of git config files

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

