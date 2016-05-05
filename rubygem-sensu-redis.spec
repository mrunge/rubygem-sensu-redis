# Generated from sensu-redis-1.3.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sensu-redis

Name:           rubygem-%{gem_name}
Version:        1.3.0
Release:        1%{?dist}
Summary:        The Sensu Redis client library
Group:          Development/Languages
License:        MIT
URL:            https://github.com/sensu/sensu-redis
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:         0001-Remove-code-climate-dependency.patch

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby
BuildRequires:  rubygem(eventmachine)
#BuildRequires:  rubygem(rspec)
#BuildRequires: rubygem(codeclimate-test-reporter)
BuildArch:      noarch

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
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%patch0 -p1

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


# Run the test suite
%check
pushd .%{gem_instdir}
# XXX: Skip running test suite as it currently expects running Redis instance
#rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/sensu-redis.gemspec
%{gem_instdir}/spec

%changelog
* Wed May 04 2016 Martin Mágr <mmagr@redhat.com> - 1.3.0-1
- Initial package
