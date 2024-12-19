%define git 20241130

Name:           sd.cpp.gui.wx 
Version:        0.2.3
Release:        1
Summary:        Stable Diffusion GUI written in C++ 
License:        MiT
URL:            https://github.com/fszontagh/sd.cpp.gui.wx/
Source0:        https://github.com/fszontagh/sd.cpp.gui.wx/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake(CpuFeatures)
BuildRequires:	cmake(libzip)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(openblas)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  glslang-devel
BuildRequires:  pkgconfig(shaderc)
BuildRequires:  glslc
BuildRequires:  wxwidgets-devel
BuildSystem:	cmake

%patchlist
https://github.com/fszontagh/sd.cpp.gui.wx/commit/96762bb206ccdfd5ed78d523d01d6158f82c2ffa.patch


%description
A cross-platform GUI for Stable Diffusion C++, built using wxWidgets.

Licensed under the MIT License.
Features

    Text-to-image (text2img) generation
    Image-to-image (img2img) generation
    Built-in upscaling capabilities
    ControlNet integration
    Model conversion to GGUF format
    Optional integration with CivitAi Model Downloader
    Hardware detection for optimal diffusion performance
    Integrated model management tools
    VAE support
    Customizable generation presets
    Generation queue for batch processing
    Real-time progress monitoring during generation
    Save and load metadata directly from images
    Multi-language GUI support

Supported Backends:
    CPU (AVX, AVX2, AVX512)
    CUDA
    ROCm
* Vulkan


%prep
%autosetup -n %{name}-%{version} -p1

%files
%license LICENSE
%doc README.md
