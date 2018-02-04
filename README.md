# Typograf Service

It's typograf service for Russian texts.
That's program check text for the next conditions and correct it:
* remove extra space and tabs
* remove extra linebreak
* replace ' or " to « »
* replacement of hyphens with dashes in phone numbers
* connect numbers with words by non-breaking space
* replacing dashes on hyphens
* replacing hyphens on dashes
* connect conjunctions and any words by non-breaking space

# How to install
```bash
$pip install -r requirements.txt
```

# How to use
```bash
$python server.py

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

# Example
### Original text
```
Так вот, это дерево, потом идут  лишние     пробелы(табы). А наш номер +700-233-22-11111 который
Это очень "большое" дерево.  
  
  
мы купили за 1000 рублей. Во во говорил я тогда
```
### Result
```
Так вот, это — дерево, потом идут лишние пробелы(табы). А наш номер +700-233-22-11111 который
Это — очень «большое» дерево.
мы купили за 1000 рублей. Во во говорил я тогда
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
