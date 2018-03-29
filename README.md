## Make Sreracha work again!

To make Sreracha application work as described in the document the following steps were taken:

- Fixed the apk installs to install clean and update cert store
- Make the `srearacha` binary executable
- Add redis db container
- Add `REDIS_URL` environment variable to sreracha application Dockerfile
- Have `sreracha` run as root user instead of www user (since it was expecting privileged port 80)
- Bundle it all up with docker-compose
- Yay! we got a [200](/q_is_for_query.png)!

## Junior take notice

According to our findings, the sreracha application is a [Go](https://golang.org/) binary.  
The application code seems to be running the [Fizzbuzz](https://www.tomdalling.com/blog/software-design/fizzbuzz-in-too-much-detail/) exercise!  
From repeated runs, it seems there is a consistent bug in the code causing a kernel panic at the exact stage when the application gets to number 30.  
As can be seen in [this](/tuboencabulate.png) screenshot  
The file producing the bug is `sreracha.go` and line of code is [42](https://en.wikipedia.org/wiki/Phrases_from_The_Hitchhiker%27s_Guide_to_the_Galaxy#The_number_4")  

## FizzBuzzerz

The sreracha application seems to be trying to run version of the FizzBuzz programming challenge.  
However, by the output we can see in [this](/tuboencabulate.png) screenshot we can see a major bug in the code that results in output different than the rules.  
  
Here are the results of [this](/fizzbuzz.py) simple Python fizzbuzz implementation that receives an integer parameter maximum until which to run the FizzBuzz rules.

```
./fizzbuzz.py 32
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
16
17
fizz
19
buzz
fizz
22
23
fizz
buzz
26
fizz
28
29
fizzbuzz
31
32 
```

However, in the `sreracha` app we can see this output: `SET 15 Fizz: OK` which should be FizzBuzz since it divides by both 3 and 5.  

This seems to show that the logic of the app was implemented by first checking if the number is divisible by three and immediately printing "Fizz" if that is true instead of checking if it *_ALSO_* divides by 5 and then should merit the output `FizzBuzz`