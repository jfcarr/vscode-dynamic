sub say_hello {
    my ($name) = @_;

    print "Hello, $name!\n";
}

sub get_square {
    my ($input_val) = @_;

    return $input_val * 2;
}

say_hello("Jim");

my $square_value = get_square(2);
print "The square is $square_value\n";
