#coder :- HomeAutomationSystemBot



import sys
import time
import telepot
import RPi.GPIO as GPIO
#LED

l=0
f=0
r=0

def on(pin):
    GPIO.output(pin,GPIO.LOW)
    global l
    l=1
    print("Pin 8 is high\n")
    return "Bhoom Led On :-) Thank You For Using HomeAutomationSystemBot To Turn Off LED Type Off\n"
def off(pin):
    GPIO.output(pin,GPIO.HIGH)
    global l
    l=0
    print("Pin 8 is low\n")
    return "Bhoom Led Off :-) Thank You For Using HomeAutomationSystemBot To Turn Off LED Type On\n"

def MotorOnF(m1,m2):
    GPIO.output(m1,GPIO.HIGH)
    GPIO.output(m2,GPIO.LOW)
    global f
    f=1
    global r
    r=0
    print("Motor rotating in Forward direction\n")
    print("Pin 10 is High\n")
    print("Pin 12 is Low\n")
    return "Motor rotating in Forward direction"
def MotorOnR(m1,m2):
    GPIO.output(m1,GPIO.LOW)
    GPIO.output(m2,GPIO.HIGH)
    global f
    f=0
    global r
    r=1
    print("Motor rotating in reverse direction\n")
    print("Pin 10 is LOW\n")
    print("Pin 12 is HIGH\n")
    return "Motor rotating in reverse direction"
def MotorOff(m1,m2):
    GPIO.output(m1,GPIO.LOW)
    GPIO.output(m2,GPIO.LOW)
    global f
    f=0
    global r
    r=0
    print("Pin 10 is Low\n")
    print("Pin 12 is Low\n")
    return "Motor is turned off"
def Status():
    s=""
    global l
    global f
    global r
    print( l, f, r)
    if( l==1):
        s="Ligth is ON "
    else:
        s="Ligth is OFF "
    if(( f==1 and  r==0) or ( f==1 and  r==0)):
        s+=" Motor is ON"
    else:
        s+=" Motor is OFF"
    return s
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# set up GPIO output channel
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

#default values

GPIO.output(8,GPIO.HIGH)
GPIO.setup(10, GPIO.LOW)
GPIO.setup(12, GPIO.LOW)

def handle(msg):
    chat_id = msg["chat"]["id"]
    command = msg["text"]

    print("Got command: %s" % command)

    if command.lower() == "on":
        bot.sendMessage(chat_id, on(8))
    elif command.lower() =="off":
        bot.sendMessage(chat_id, off(8))
    elif command.lower() == "motoronf":
        bot.sendMessage(chat_id, MotorOnF(10,12))
    elif command.lower() == "motoronr":
        bot.sendMessage(chat_id, MotorOnR(10,12))
    elif command.lower() == "motoroff":
        bot.sendMessage(chat_id, MotorOff(10,12))
    elif command.lower() == "status":
        bot.sendMessage(chat_id, Status())

    elif command =="stop":
        x="process is stopped please re run the program again ----> :-) \n"
        bot.sendMessage(chat_id,x)
        GPIO.cleanup()
        quit()

bot = telepot.Bot("5067977957:AAFClOotjEtnLGP-c4qQZVWQF7zI61qwsy4") 
bot.message_loop(handle)
print("Yes EtherPiBot is ALive ....EthePiBot is listening...\n")
while 1:
    try:
        time.sleep(10)
    except KeyboardInterrupt:
        print("\n Program interrupted")
        GPIO.cleanup()
        exit()
    except:
        print("Other error or exception occured!")
        GPIO.cleanup()
