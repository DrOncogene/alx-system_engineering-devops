# kill a command called killmenow
exec { 'killmenow':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => 'pkill killmenow',
  onlyif  => "test 'pgrep killmenow | wc -l' -gt 0"
}
