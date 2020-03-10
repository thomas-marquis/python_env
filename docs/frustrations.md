# Frustrations liées au langage python

## Problèmes

- [la performance](https://ilovesymposia.com/2015/12/10/the-cost-of-a-python-function-call/), l'interpréteur python
 est lent. Pour de la perf, il faut utiliser des libs implémentées en C. Ce qui implique des process de build supplémentaires...
- [Le global interpreter lock (GIL)](https://medium.com/@natemurthy/all-the-things-i-hate-about-python-5c5ff5fda95e) qui 
interdit le vrais multithreading. Python n'execute qu'un seul thread à la fois


## Solutions

**les problèmes de perf**

- utiliser Jython ???
- implémenter les libs crutiales en c (interopérabilité entre les deux langages ???)


## ressources

- [tout savoir sur le calcul distribué en python](http://www.dabeaz.com/usenix2009/concurrent/)
