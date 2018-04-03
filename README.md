# Web Printer
A user friendly web printing service.

### What's that?
You can know it from the name. It's a web service, to which you upload pdf file and it will print the pdf using the physical printer connected to it.

### But why I need it?
You may already have a fancy printer with cutting-edge wireless printing function, but sadly, we don't. To be specific, the old fashioned printer in my lab is manufactured at 2006 and its network printing is showing its age (even the smartest guy in our lab cannot properly config it).

Apart from this, we want a web service which can properly handle remote printing requests without pain.

### How to setup?
Well, the service is deployed on a Mac next to the printer but technically, you may deploy it on any Linux machine. If you happened to use Windows, you are definitely smart enough to install a linux virtual machine and attach the printer to it :)

A basic config template can be found at `config_sample.py`. It is a good idea to start from editing this file with your requirement. Then, what you need to start it in the same way as any starting any other flask app.
