%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           PyOpenGL
Version:        3.0.0
Release:        2.1%{?dist}
Summary:        Python bindings for OpenGL
License:        BSD
Group:          System Environment/Libraries
URL:            http://pyopengl.sourceforge.net/
Source0:        http://downloads.sourceforge.net/pyopengl/%{name}-%{version}.tar.gz
Patch0:         PyOpenGL-3.0.0a6-shebang.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  python-devel python-setuptools-devel
BuildArch:      noarch
Requires:       numpy python-setuptools freeglut
# in some other repositories this is named python-opengl
Provides:       python-opengl = %{version}-%{release}
Obsoletes:      python-opengl < %{version}-%{release}

%description
PyOpenGL is the cross platform Python binding to OpenGL and related APIs. It
includes support for OpenGL v1.1, GLU, GLUT v3.7, GLE 3 and WGL 4. It also
includes support for dozens of extensions (where supported in the underlying
implementation).

PyOpenGL is interoperable with a large number of external GUI libraries
for Python including (Tkinter, wxPython, FxPy, PyGame, and Qt). 


%package Tk
Summary:        %{name} OpenGL Tk widget
Group:          System Environment/Libraries
Requires:       %{name} = %{version}-%{release}, tkinter

%description Tk
%{name} Togl (Tk OpenGL widget) 1.6 support.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -z .shebang

%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root="$RPM_BUILD_ROOT" \
  --prefix="%{_prefix}"
chmod -x $RPM_BUILD_ROOT%{python_sitelib}/%{name}-%{version}-py?.?.egg-info


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{python_sitelib}/*OpenGL*
%exclude %{python_sitelib}/OpenGL/Tk

%files Tk
%defattr(-,root,root,-)
%{python_sitelib}/OpenGL/Tk

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 3.0.0-2.1
- Rebuilt for RHEL 6

* Thu Jul 30 2009 Jesse Keating <jkeating@redhat.com> - 3.0.0-2
- Rebuild for Fedora 12 mass rebuild

* Tue Jun 9 2009 Nikolay Vladimirov <nikolay@vladimiroff.com> - 3.0.0-1
- Updated to 3.0 stable
- Changed requires from python-numeric to numpy for BZ #504681
- upstream removed full license text in license.txt
- other minor spec fixes

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-0.12.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 2 2009 Nikolay Vladimirov <nikolay@vladimiroff.com> - 3.0.0-0.11.b8
- New upstream 3.0.0b8 (b7 was skipped by upstream)
- performance, bug-fix and packaging release. 
- Use macro for "python"
- remove "--single-version-externally-managed" option for setup.py
- *.egg-info is no longer a folder, it's a file now 
- Tests are no longer installed by setup.py
- Obsolete 'doc' subpackage (no longer distributed "documentation" folder)
- license.txt is also no longer provided by upstream. Using one from b6
- Removed Requires for libGL and libGLU ( should be pulled for freeglut)

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.0.0-0.10.b6
- Fix locations for Python 2.6

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.0.0-0.9.b6
- Rebuild for Python 2.6

* Mon Sep 22 2008 Nikolay Vladimirov <nikolay@vladimiroff.com> 3.0.0-0.8.b6
- New upstream release 3.0.0b6

* Mon Jul 28 2008 Nikolay Vladimirov <nikolay@vladimiroff.com> 3.0.0-0.7.b5
- New upstream release 3.0.0b5

* Fri Jul 18 2008 Nikolay Vladimirov <nikolay@vladimiroff.com> 3.0.0-0.6.b4
- New upstream release 3.0.0b4

* Mon Dec 31 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 3.0.0-0.5.b1
- New upstream release 3.0.0b1

* Thu Aug 30 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 3.0.0-0.4.a6
- Change BuildRequires python-setuptools to python-setuptools-devel for
  the python-setuptools package split

* Fri Apr 13 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 3.0.0-0.3.a6
- Add missing freeglut, libGL and libGLU requires (bz 236159)

* Thu Mar 29 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 3.0.0-0.2.a6
- Remove tests from the package (bz 234121)
- Add -Tk subpackage (bz 234121)
- Remove shebang from files with shebang instead of chmod +x (bz 234121)
- Better description

* Sat Mar 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 3.0.0-0.1.a6
- Initial Fedora Extras package
