# Web Printer
A user friendly web printing service.

### What's that?
The name is obvious. It's a web service, to which you upload pdf file and it will print the pdf using the physical printer connected to it.

### But why I need it?
You may already have a fancy printer with cutting-edge wireless printing function, but sadly, we don't. To be specific, the old fashioned printer in my lab was manufactured at 2006 and the network printing proto is showing its age (even the smartest guy in our lab cannot properly config it).

Apart from this, we want a web service which can properly handle remote printing requests without pain.

### How to setup?
Well, the service is deployed on a Mac next to the printer but technically, you may deploy it on any Unix machine. If you happened to use Windows, you are definitely smart enough to install a linux virtual machine and attach the printer to it :)

A basic config template can be found at `config_sample.py`. It is a good idea to start editing this file with your requirement. Then, you only need to start it in the same way as other flask apps.
