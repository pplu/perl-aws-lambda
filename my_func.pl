#!/usr/bin/env perl

use strict;
use warnings;

use ALib;

my $x = ALib->new(5);

print '{"x":' . $x->x . '}';
