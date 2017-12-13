%global modname git
%global srcname GitPython

Name:           %{srcname}
Version:        2.1.8
Release:        1%{?dist}
Summary:        Python Git Library

License:        BSD
URL:            https://github.com/gitpython-developers/GitPython
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
GitPython is a python library used to interact with git repositories,\
high-level like git-porcelain, or low-level like git-plumbing.\
\
It provides abstractions of git objects for easy access of repository data,\
and additionally allows you to access the git repository more directly using\
either a pure python implementation, or the faster, but more resource\
intensive git command implementation.\
\
The object database implementation is optimized for handling large quantities\
of objects and large datasets, which is achieved by using\
low-level structures and data streaming.

%description %{_description}

%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       git-core
Requires:       python2-gitdb >= 2.0.0

# Old name
Provides:       %{srcname} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{srcname} < %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python2-%{srcname} %{_description}

Python 2 version.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       git-core
Requires:       python3-gitdb >= 2.0.0

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%files -n python2-%{srcname}
%license LICENSE
%doc CHANGES AUTHORS
%{python2_sitelib}/%{srcname}-*.egg-info/
%{python2_sitelib}/%{modname}/

%files -n python3-%{srcname}
%license LICENSE
%doc CHANGES AUTHORS
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%changelog
* Wed Dec 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.8-1
- Update to 2.1.8

* Wed Nov 01 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.7-2
- Fix interaction with git 2.15

* Sat Sep 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.7-1
- Update to 2.1.7

* Tue Aug 08 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.5-1
- Update to 2.1.5

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 11 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.1.3-1
- Update to 2.1.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.1.1-2
- Provide/Obsolete old name

* Wed Dec 28 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.1.1-1
- Update to 2.1.1
- Modernize spec

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-2
- Rebuild for Python 3.6

* Tue Nov 29 2016 Lubomír Sedlář <lsedlar@redhat.com> - 2.1.0-1
- New upstream release

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

