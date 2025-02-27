### Do TCP attack
1. Set up the free5gc testbed, do all steps up to 5.

2. Do this command from the scripts folder:

```bash
kubectl cp -n free5gc tcp.py free5gc-smf1-949b5698d-2vl5q:/free5gc/tcp.py
```

This copys the file into the smf pod.

3. Then go into the shell of the smf pod from the free5gc-k8s folder.

```bash 
cd bin
./k8s-shell.sh smf1 
```

4. Install python 3.13:

```bash 
apt update
```

```bash 
apt-get install software-properties-common -y
```

```bash 
add-apt-repository ppa:deadsnakes/ppa
```

```bash 
apt install python3.13
```

5. install pip (python package manager):

```bash
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.13
```
6. install scapy:

```bash
pip install scapy
```

7. try script out:


### Attack No 1.
This is how we do attack no 1:

