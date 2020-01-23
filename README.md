# ONOS mininet sdn setup guide

For this lab i am using VirtualBox 6.1.0 r135406 on Windows 10 home 1909. This is how i configured my virtual machine.

    Ubuntu 18.04 LTS x64
    CPU - Intel® Core™ i7-8750H CPU @ 2.20GHz × 3 cores
    RAM - 3GB 
    disk - 22.9GB 
    network - NAT,Host-Only adapter


## Installed packages (follow these steps in order when installing)

**Mininet 2.2.2**

    sudo apt-get update
    sudo apt-get install mininet -y



**JDK 11.0.6** - required to run ONOS, don't install JDK SE 8 it gave me some strange errors in ONOS. use this tutorial to install JDK [https://www.javahelps.com/2017/09/install-oracle-jdk-9-on-linux.html](https://www.javahelps.com/2017/09/install-oracle-jdk-9-on-linux.html), to verify your installed java version enter _java --version_ in a terminal window.

    java --version
        `java 11.0.6 2020-01-14 LTS
        Java(TM) SE Runtime Environment 18.9 (build 11.0.6+8-LTS)
        Java HotSpot(TM) 64-Bit Server VM 18.9 (build 11.0.6+8-LTS, mixed mode)`



**ONOS 2.2.0** (follow these steps to setup onos)

    sudo su
    cd /opt
    wget https://repo1.maven.org/maven2/org/onosproject/onos-releases/2.2.0/onos-2.2.0.tar.gz
    tar -xvzf onos-2.2.0.tar.gz
    mv onos-2.2.0 onos
    cd onos/bin/
    ./onos-service start
  
Use this link to activate below mentions application in ONOS.(onos -> applications -> search and activate) 

_ONOS web interface_ [http://127.0.0.1:8181/onos/ui/](http://127.0.0.1:8181/onos/ui/)   

    org.onosproject.drivers              Default Drivers
    org.onosproject.optical-model        Optical Network Model
    org.onosproject.openflow-base        OpenFlow Base Provider
    org.onosproject.lldpprovider         LLDP Link Provider
    org.onosproject.hostprovider         Host Location Provider
    org.onosproject.openflow             OpenFlow Provider Suite
    org.onosproject.fwd                  Reactive Forwarding
    org.onosproject.gui2                 ONOS GUI2

  
Open new terminal window, use password "karaf" and verify activated apps 

_ONOS cli_

      ssh -p 8101 karaf@localhost
      apps -a -s
      
  output should be similar to this

    *  17 org.onosproject.drivers              2.2.0    Default Drivers
    *  18 org.onosproject.optical-model        2.2.0    Optical Network Model
    *  46 org.onosproject.openflow-base        2.2.0    OpenFlow Base Provider
    *  47 org.onosproject.lldpprovider         2.2.0    LLDP Link Provider
    *  48 org.onosproject.hostprovider         2.2.0    Host Location Provider
    *  64 org.onosproject.openflow             2.2.0    OpenFlow Provider Suite
    *  84 org.onosproject.fwd                  2.2.0    Reactive Forwarding
    * 185 org.onosproject.gui2                 2.2.0    ONOS GUI2



## To test the sdn.py (use currect directory path), open new terminal window. 

    sudo mn -c
    sudo -E python sdn.py 
    pingall

Refresh after ONOS web interface after runnig _pingall_ command.

Good Luck

*i created this for a coursework*
