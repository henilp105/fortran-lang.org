## bessel\_y0
### __Name__

__bessel\_y0__(3) - \[MATHEMATICS\] Bessel function of the second kind of order 0


### __Syntax__
```fortran
    result = bessel_y0(x)
```
### __Description__

__bessel\_y0(x)__ computes the Bessel function of the second
kind of order 0 of __x__.

### __Arguments__

  - __x__
    : The type shall be _real_.

### __Returns__

The return value is of type _real_. It has the same kind as __x__.

### __Examples__

Sample program:

```fortran
program demo_besy0
use, intrinsic :: iso_fortran_env, only : real_kinds, &
& real32, real64, real128
implicit none
  real(kind=real64) :: x = 0.0_real64
  x = bessel_y0(x)
  write(*,*)x
end program demo_besy0
```
  Results:
```text
                    -Infinity
```

### __Standard__

Fortran 2008 and later

### __See Also__

[__bessel\_j0__(3)](BESSEL_J0),
[__bessel\_j1__(3)](BESSEL_J1),
[__bessel\_jn__(3)](BESSEL_JN), 
[__bessel\_y1__(3)](BESSEL_Y1), 
[__bessel\_yn__(3)](BESSEL_YN)

####### fortran-lang intrinsic descriptions
