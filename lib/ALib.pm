package ALib;

use strict;
use warnings;

sub new {
  my ($class, $x) = @_;
  return bless ({ x => $x }, $class);
}

sub x {
  return shift->{ x };
}

1;
