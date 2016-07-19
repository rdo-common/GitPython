%if 0%{?fedora}
%global with_python3 1
%endif
%if 0%{?rhel} && 0%{?rhel} <= 7
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%else
%global with_python3 1
%endif

Name:           GitPython
Version:        1.0.1
Release:        6%{?dist}
Summary:        Python Git Library

Group:          Development/Languages
License:        BSD
URL:            http://pypi.python.org/pypi/GitPython/
Source0:        http://pypi.python.org/packages/source/G/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel python-setuptools
Requires:       git-core
Requires:       python-gitdb

%description
GitPython is a python library used to interact with Git repositories.

GitPython provides object model access to your git repository. Once you have
created a repository object, you can traverse it to find parent commit(s),
trees, blobs, etc.

GitPython is a port of the grit library in Ruby created by Tom Preston-Werner
and Chris Wanstrath.

%if %{with python3}
%package -n python3-GitPython
Summary:        Python3 Git Library
Requires:       git-core
Requires:       python3-gitdb
BuildRequires:  python3-devel python3-setuptools

%description -n python3-GitPython
%{description}
%endif

%prep
%setup -qc
mv %{name}-%{version} python2

%if 0%{?with_python3}
cp -a python2 python3
find python3 -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif # with_python3

find python2 -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'

pushd python2
cp AUTHORS CHANGES LICENSE ../
popd

%build
pushd python2
%{__python2} setup.py build
popd

%if %{with python3}
pushd python3
%{__python3} setup.py build
popd
%endif

%install
pushd python2
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
popd
%if %{with python3}
pushd python3
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
popd
%endif

%files
%license LICENSE
%doc CHANGES AUTHORS
%{python2_sitelib}/GitPython-%{version}-py?.?.egg-info
%{python2_sitelib}/git/

%if %{with python3}
%files -n python3-GitPython
%license LICENSE
%doc CHANGES AUTHORS
%{python3_sitelib}/GitPython-%{version}-py?.?.egg-info
%{python3_sitelib}/git/
%endif

%changelog
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 27 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.1-4
- Require git-core

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 31 2015 Dennis Gilmore <dennis@ausil.us> - 1.0.1-1
- Update to 1.0.1
- Add python3 build

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-0.7.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

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

