# Using Puppet, install puppet-lint.

exec { 'gem install':
  command => '/usr/bin/gem install puppet-lint -v 2.1.1'
}
