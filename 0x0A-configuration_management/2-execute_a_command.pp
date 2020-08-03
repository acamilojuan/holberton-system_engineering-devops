# Using Puppet, the manifest kills a process named killmenow

exec { 'pkill':
  command => '/usr/bin/pkill killmenow'
}
