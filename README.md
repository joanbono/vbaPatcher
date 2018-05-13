# vbaPatcher

Simple script which patches an Office document with password-protected macros.

***

## Requirements

+ [`radare2`](http://radare.org/)
+ [`r2pipe-python`](https://github.com/radare/radare2-r2pipe/tree/master/python)

***

## Usage

~~~bash
git clone https://github.com/joanbono/vbaPatcher
cd vbaPatcher/src
python vbaPatcher.py vbaProject.bin
~~~

![](img/vbaPatcher.png)

***

## References

See [**Analyzing a suspicious email**](https://joanbono.github.io/PoC/Suspicious_email.html)
