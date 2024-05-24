```sh
python 2-lab-3.py generate_keys 1
```

```sh
python 2-lab-3.py encrypt "msg" ./public-rsa.pem
```

```sh
python 2-lab-3.py decrypt "Ntq8GGDcOTPTGH8yq2V4PAqZ/2omLcwJwLDA4D8IfnDa3YbKNygAegZgAhkmO8OiWoSaiYLxhBiP4L8rnaEkgbNMRiB1qgUSZrRWzbVqMytCClfP8/G0wTueud/x81MCwxhMdPhEX8EjB3lgHr5VGjVU5aXp9kVWeKVIvPZmOao=" ./private-rsa.pem
```

```sh
python 2-lab-3.py sign "content" ./private-rsa.pem
```

```sh
python 2-lab-3.py verify "content" "AoEJxjnYah5Y90MG51PtH/qi2RqANzeORUg0YKYSR0Ia1mO9Ru7Vi+fR2lHxDWABL9eLe/QzZwf9EbPz1N+RJVUg1JcqfGScgdVNUG7b8vPiaOhiSV3cRpjwsJ24SehTm/I9EA3u44DOVkdGxixaGxau6pBe4oG+GB/ptkvLSG0=" ./public-rsa.pem
```
