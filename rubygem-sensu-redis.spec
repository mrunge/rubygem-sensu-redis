# Generated from sensu-redis-1.3.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sensu-redis

Name:           rubygem-%{gem_name}
Version:        2.1.0
Release:        2%{?dist}
Summary:        The Sensu Redis client library
Group:          Development/Languages
License:        MIT
URL:            https://github.com/sensu/sensu-redis
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
#Source1:        https://github.com/sensu/%{gem_name}/archive/v%{version}.tar.gz#/%{gem_name}-%{version}.tar.gz

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby
BuildRequires:  rubygem(eventmachine)
#BuildRequires:  rubygem(rspec)
BuildArch:      noarch

Requires:       rubygem(eventmachine)

%if 0%{?rhel} > 0
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
The Sensu Redis client library.


%package doc
Summary:        Documentation for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}
%if 0%{?dlrn} > 0
%setup -q -D -T -n  %{dlrn_nvr}
%else
%setup -q -D -T -n  %{gem_name}-%{version}
%endif
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

#install -d -p %{_builddir}%{gem_instdir}
#%if 0%{?dlrn} > 0
#tar -xvzf %{SOURCE1} -C %{_builddir}/%{dlrn_nvr}/%{gem_instdir} --strip-components=1 %{gem_name}-%{version}/spec
#%else
#tar -xvzf %{SOURCE1} -C %{_builddir}/%{gem_name}-%{version}/%{gem_instdir} --strip-components=1 %{gem_name}-%{version}/spec
#%endif

# Run the test suite
%check
pushd .%{gem_instdir}
# XXX: Skip running test suite as it currently expects running Redis instance
#rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/sensu-redis.gemspec

%changelog
* Fri Dec 23 2016 Martin Mágr <mmagr@redhat.com> - 2.1.0-1
- Update to latest upstream release

* Mon May 09 2016 Martin Mágr <mmagr@redhat.com> - 1.3.0-2
- Explicitly list provides for RHEL
- Add missing runtime dependency

* Wed May 04 2016 Martin Mágr <mmagr@redhat.com> - 1.3.0-1
- Initial package
