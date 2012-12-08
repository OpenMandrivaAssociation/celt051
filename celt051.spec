%define oname celt
%define version 0.5.1.3
%define release 1
%define libversion 051
%define major 0
%define name celt%{libversion}
%define libname %mklibname %{oname} %{libversion} %{major}
%define develname %mklibname -d %{oname} %{libversion}
%define oldlibname %mklibname %{oname} 0 0

Summary: Ultra-low delay audio codec
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://downloads.us.xiph.org/releases/celt/%{oname}-%{version}.tar.gz
License: BSD
Group: Sound
Url: http://www.celt-codec.org/
BuildRequires: libogg-devel

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
Summary: Ultra-low delay audio codec - shared library
Group: System/Libraries
Obsoletes: %{oldlibname} < 0.5.1.3-2

%description -n %{libname}
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

%package -n %develname
Summary: Headers for developing programs that will use %{name}
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.


%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README TODO
%{_bindir}/celtenc051
%{_bindir}/celtdec051

%files -n %libname
%doc README COPYING
%_libdir/lib%{name}.so.%{major}
%_libdir/lib%{name}.so.%{major}.*

%files -n %develname
%_includedir/%{name}
%_libdir/pkgconfig/%name.pc
%_libdir/lib%{name}.so
%_libdir/lib%{name}.a



%changelog
* Fri May 04 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.5.1.3-1
+ Revision: 795967
- imported package celt051

