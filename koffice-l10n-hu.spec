Name: koffice-l10n-hu
Version: 2.3.2
Release: %mkrel 2
Summary: Language files for KOffice Hungarian
Group: System/Internationalization
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPLv2+
URL: https://www.koffice.org
BuildArch: noarch
Source: ftp://ftp.kde.org/pub/kde/stable/koffice-%version/src/koffice-l10n/%name-%version.tar.bz2
BuildRequires: gettext >= 0.15
BuildRequires: kdelibs4-devel
Requires: locales-hu
Requires: koffice-core
Provides: koffice-l10n

%description 
Provides Hungarian translations for KOffice.

%files 
%defattr(-,root,root,-)
%{_kde_datadir}/*/*/*

#------------------------------------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %buildroot


%changelog
* Sat Feb 26 2011 Funda Wang <fwang@mandriva.org> 2.3.2-2mdv2011.0
+ Revision: 639859
- rebuild

* Fri Feb 18 2011 Funda Wang <fwang@mandriva.org> 2.3.2-1
+ Revision: 638330
- New version 2.3.2

* Thu Jan 20 2011 Funda Wang <fwang@mandriva.org> 2.3.1-1
+ Revision: 631766
- New version 2.3.1

* Thu Dec 30 2010 Funda Wang <fwang@mandriva.org> 2.3.0-1mdv2011.0
+ Revision: 626267
- New version 2.3.0

* Thu Dec 09 2010 Funda Wang <fwang@mandriva.org> 2.2.91-1mdv2011.0
+ Revision: 617999
- New version 2.2.91

* Thu Nov 18 2010 Funda Wang <fwang@mandriva.org> 2.2.84-1mdv2011.0
+ Revision: 598546
- New version 2.2.84

* Fri Oct 29 2010 Funda Wang <fwang@mandriva.org> 2.2.83-1mdv2011.0
+ Revision: 589874
- New version 2.2.83

* Sat Jan 17 2009 Funda Wang <fwang@mandriva.org> 1.9.98.5-1mdv2009.1
+ Revision: 330490
- new version 1.9.98.5

* Thu Dec 11 2008 Funda Wang <fwang@mandriva.org> 1.9.98.3-1mdv2009.1
+ Revision: 312727
- new version 1.9.98.3

* Thu Nov 20 2008 Funda Wang <fwang@mandriva.org> 1.9.98.2-1mdv2009.1
+ Revision: 305046
- add source and spec
- Created package structure for koffice-l10n-hu.


* Fri Feb 16 2007 Laurent Montel <lmontel@mandriva.com> 1.6.2-1mdv2007.0
+ Revision: 121722
- 1.6.2

* Thu Nov 30 2006 Laurent Montel <lmontel@mandriva.com> 1.6.1-1mdv2007.1
+ Revision: 88943
- 1.6.1

* Thu Nov 02 2006 Laurent Montel <lmontel@mandriva.com> 1.6.0-1mdv2007.1
+ Revision: 75126
- 1.6.0
- Import koffice-l10n-hu

* Sun Jul 16 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5.2-1
- 1.5.2

* Thu Jul 13 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5.1-3
- Requires koffice-apps

* Sun May 28 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5.1-2
- Use %%mkrel

* Thu May 25 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5.1-1mdk
- 1.5.1

* Thu Apr 13 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5.0-1mdk
- 1.5.0

* Fri Mar 31 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5-0.rc1.1mdk
- 1.5.0-rc1

* Tue Oct 18 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4.2-1mdk
- 1.4.2

* Sat Aug 13 2005 Laurent MONTEL <lmontel@mandriva.com> 20mdk
- Remove conflict with kde-i18n

* Fri Jul 29 2005 Laurent MONTEL <lmontel@mandriva.com> 10mdk
- Fix provides koffice-l10n

* Tue Jul 26 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4.1-1mdk
- 1.4.1

* Sat Jun 18 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4.0-1mdk
- 1.4.0

* Wed Apr 20 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.91-1mdk
- 1.3.91

* Wed Nov 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.5-1mdk
- 1.3.5

* Thu Oct 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.4-1mdk
- 1.3.4

* Wed Sep 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.3-1mdk
- 1.3.3

* Tue Jul 06 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.2-1mdk
- 1.3.2

* Wed May 05 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.1-1mdk
- 1.3.1

