
use strict;
use DE_EPAGES::TLE::API::TLE qw ( TestSyntax );


my $Content = '';
my @Lines = ();

while (<>) {
    $Content .= $_;
    push @Lines, $_;
}

my $Error = TestSyntax(\$Content);

if ($Error) {
    my $Message = $Error->vars->{'Message'};

    my @Yyparse = split(/\n/, $Error->vars->{'yyparse'});
    my $AfterNear = $Yyparse[0];
    my $QuotedAfterNear = quotemeta($AfterNear);

    my $LineNumber = $Error->vars->{'Line'};
    my $Line = $Lines[$LineNumber - 1];
    my @ParsedLine = split(/$QuotedAfterNear/, $Line);
    my $Near = $ParsedLine[0];
    $Near =~ s/^\s*//;

    print "$Message at line $LineNumber, near $Near";
}
else {
    print "syntax ok\n";
}
