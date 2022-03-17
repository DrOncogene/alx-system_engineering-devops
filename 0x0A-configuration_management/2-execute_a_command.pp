# kill a command called killmenow
exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
}
