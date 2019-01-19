# Bills-to-text

This project aims to read and extract information from a `Nota Fiscal` (brazilian receipt) photo.

## Installing

> Install tesseract

### MAC OSX

```sh
$ brew install tesseract
```

### Linux (Debian/Ubuntu based)
```sh
$ sudo apt update
$ sudo apt install tesseract-ocr
$ sudo apt install libtesseract-dev
```

> Install dependencies

```sh
$ pip install -r requirements.txt
```

## TO DO

> That's actually just a POC for now

- [ ] Implement flask server for endpoints
- [ ] Implement a way to read different files over rest
- [ ] Implement output formatter
