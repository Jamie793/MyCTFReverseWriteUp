import frida
import sys

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

jscode = """
Java.perform(function () {
    console.log("Running...")
    var MainActivity = Java.use('net.bluelotus.tomorrow.easyandroid.MainActivity')

    MainActivity.onCreate.overload('android.os.Bundle').implementation = function(p1){
        console.log(this);
        this.k.value = 1616384;
        send(this.stringFromJNI2(0));
        send(this);
        this.onCreate(p1);
    }

});
"""


rdev = frida.get_remote_device()
pid = rdev.spawn('net.bluelotus.tomorrow.easyandroid')
session = rdev.attach(pid)
rdev.resume(pid)

script = session.create_script(jscode)
script.on('message', on_message)
script.load()
sys.stdin.read()
