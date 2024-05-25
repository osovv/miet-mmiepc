```sh
openssl genrsa -out al.localhost.key 2048
```

```sh
openssl req -new -key al.localhost.key -out al.localhost.csr -subj "/CN=al.localhost/O=Example LLC/C=US"
```

```sh
days=$(python -c "import datetime; print((datetime.datetime.now().date().replace(month=12, day=31) - datetime.date.today()).days)")
```

```sh
echo $days
```

```sh
openssl x509 -req -days $days -in al.localhost.csr -signkey al.localhost.key -out al.localhost.crt
```

```sh
openssl x509 -in al.localhost.crt -text -noout
```
