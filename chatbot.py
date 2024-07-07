#question:answer
import time
now = time.ctime()
qna={
    "hi":"hey",
    "how are u":"I am fine",
    "what is your name":"my name is bani",
    "how old are you":"i am 20 years old",
    "what is the time now":now,
}
while True:
    qs=input()
    if(qs=="quit"):
        break
    else:
        print(qna[qs])