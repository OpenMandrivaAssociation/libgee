%global optflags %{optflags} -Wno-incompatible-function-pointer-types

%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

%define api	0.8
%define major	2
%define libname %mklibname gee %{api} %{major}
%define girname %mklibname gee-gir %{api}
%define devname %mklibname -d gee

Summary:	GObject-based collection library
Name:		libgee
Version:	0.20.6
Release:	4
License: 	LGPLv2+
Group:		System/Libraries
Url: 		https://live.gnome.org/Libgee
Source0: 	https://ftp.gnome.org/pub/GNOME/sources/libgee/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)

%description
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

%package -n	%{libname}
Summary:	Collection library providing GObject-based interfaces and classes
Group:		%{group}

%description -n	%{libname}
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n	%{devname}
Summary:	Libraries and include files for developing with libgee
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package provides the necessary development libraries and include
files to allow you to develop with libgee.

%prep
%setup -q

%build
%configure

%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libgee-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Gee-%{api}.typelib

%files -n %{devname}
%doc AUTHORS COPYING NEWS README ChangeLog
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/vala/vapi/*.vapi
%{_datadir}/gir-1.0/Gee-%{api}.gir
