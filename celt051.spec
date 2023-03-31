%define oname	celt
%define api	051
%define major	0
%define libname	%mklibname %{oname} %{api} %{major}
%define devname %mklibname -d %{oname} %{api}

Summary:	Ultra-low delay audio codec
Name:		celt%{api}
Version:	0.5.1.3
Release:	12
License:	BSD
Group:		Sound
Url:		http://www.celt-codec.org/
Source0:	http://downloads.us.xiph.org/releases/celt/%{oname}-%{version}.tar.gz
BuildRequires:	pkgconfig(ogg)

%description
The CELT codec is an experimental audio codec for use in low-delay
speech and audio communication.

CELT stands for "Constrained Energy Lapped Transform". It applies some
of the CELP principles, but does everything in the frequency domain,
which removes some of the limitations of CELP. CELT is suitable for
both speech and music and currently features:

* Ultra-low latency (typically from 3 to 9 ms)
* Full audio bandwidth (44.1 kHz and 48 kHz)
* Support for both voice and music
* Stereo support
* Packet loss concealment
* Constant bit-rates from 32 kbps to 128 kbps and above
* A fixed-point version of the encoder and decoder

The CELT codec is meant to close the gap between Vorbis and Speex for
applications where both high quality audio and low delay are desired.

%package -n %{libname}
Summary:	Ultra-low delay audio codec - shared library
Group:		System/Libraries

%description -n %{libname}
The package contains the shared library for %{name}.

%package -n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{oname}%{api}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

%files
%doc README TODO
%{_bindir}/celtenc%{api}
%{_bindir}/celtdec%{api}

%files -n %{libname}
%_libdir/lib%{oname}%{api}.so.%{major}*

%files -n %{devname}
%doc README COPYING
%_includedir/%{oname}%{api}
%_libdir/pkgconfig/%{oname}%{api}.pc
%_libdir/lib%{oname}%{api}.so

