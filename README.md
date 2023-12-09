## Webfejlesztés project

### Fontosabb tudnivalók

#### Futtatókörnyezet

A futtatáshoz a Pycharm Community Edition-t használtam, virtuális környezetként pedig a **Python 3.10**-et.

Csomagok, amiket le kell telepíteni a megfelelő működéshez:

```
pip install django
```
```
pip install django-bootstrap-v5
```

Megjegyzem, hogy a django bootstrap a legfrissebb kiadásban volt (1.0.11), míg a django maga 4.2.8-as kiadásban.

Lehetséges, hogy a django legfrissebb verziójában is működne, de ha mégsem, akkor maradjunk a 4.2.8-nál.

#### Oldal futtatása

A terminálban az alábbi paranccsal tudjunk futtatni a környezetet:

```
python ./web_proj/manage.py runserver
```

Ezután a weboldal, ahogyan arról a terminálban is értesülünk, ezen a címen fog futni:

```
http://localhost:8000/
```