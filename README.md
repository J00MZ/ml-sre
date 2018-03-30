## Make Sreracha work again!

To make Sreracha application work as described in the document the following steps were taken:

- Fixed the apk installs to install clean and update cert store
- Make the `srearacha` binary executable
- Add redis db container
- Add `REDIS_URL` environment variable to sreracha application Dockerfile
- Have `sreracha` run as root user instead of www user (since it was expecting privileged port 80)
- Bundle it all up with docker-compose
- Yay! we got a [200](/q_is_for_query.png)!

## Prerequisites

- [docker](https://docs.docker.com/install/)
- [docker-compose](https://docs.docker.com/compose/install/)

## Running the app

```
git clone https://github.com/J00MZ/ml-sre.git
cd ml-sre
docker-compose up --build
```

## Junior take notice

According to our findings, the sreracha application is a [Go](https://golang.org/) binary.  
The application code seems to be running the [Fizzbuzz](https://www.tomdalling.com/blog/software-design/fizzbuzz-in-too-much-detail/) exercise!  
From repeated runs, it seems there is a consistent bug in the code causing a kernel panic at the exact stage when the application gets to number 30.  
As can be seen in [this](/tuboencabulate.png) screenshot  
The file producing the bug is `sreracha.go` and line of code is [42](https://en.wikipedia.org/wiki/Phrases_from_The_Hitchhiker%27s_Guide_to_the_Galaxy#The_number_4")  

## FizzBuzz (SreRacha)

The sreracha application seems to be trying to run version of the FizzBuzz programming challenge.  
However, by the output in [this](/tuboencabulate.png) screenshot there is a bug in the code that results in output different than the FizzBuzz rules.  
  
The erroneous output: `SET 15 Fizz: OK` which according to the rules should output `FizzBuzz` since 15's divisors are both 3 and 5.  
  
It seems the bug is in the implementation logic of the app.  
By first checking if the number is divisible by three and immediately printing "Fizz" if that is true.  
Instead of checking if the number *_ALSO_* divides by 5 and then should merit the output `FizzBuzz`  
  
Added [here](/fizzbuzz.py) is a strightforward Python fizzbuzz implementation that receives a single integer parameter, the maximum until which to run the FizzBuzz rules.  
  
This is an example run:

```
$ ./fizzbuzz.py 32
1
2
fizz (sre)
4
buzz (racha)
fizz (sre)
7
8
fizz (sre)
buzz (racha)
11
fizz (sre)
13
14
fizzbuzz (SreRacha!)
16
17
fizz (sre)
19
buzz (racha)
fizz (sre)
22
23
fizz (sre)
buzz (racha)
26
fizz (sre)
28
29
fizzbuzz (SreRacha!)
31
32
```
