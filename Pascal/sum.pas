program sum;

uses crt;

var
     a, b, c : Integer;

begin
     write('A: ');
     readln(a);
     write('B: ');
     readln(b);
     c:=a+b;
     writeln('C= ', c, ' <--');
     writeln();
     writeln('*press any key to exit*');
     readkey;
end.
