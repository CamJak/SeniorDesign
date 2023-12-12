# Setting up OpenWrt

## Prerequisites

- A linux machine with a working internet connection. [Ubuntu 18.04 LTS](https://ubuntu.com/download/desktop/thank-you?version=18.04.3&architecture=amd64)
- A MicroSD card with at least 8GB of storage

## Installing OpenWrt

#### 1. Clone the OpenWrt repository

```bash
git clone https://git.openwrt.org/openwrt/openwrt.git source
```
**_source_** is the name of the directory where the OpenWrt source code will be downloaded.

#### 2. Checkout the latest stable release

```bash
cd source
git tag
git checkout v23.05.2
```

#### 3. Update and install the 'feeds' packages

```bash
./scripts/feeds update -a
./scripts/feeds install -a
```

#### 4. Configure the build

```bash
make menuconfig
```

Select the following options:

```bash
Target System (Broadcom BCM27xx)
Subtarget (BCM2711 boards (64 bit))
Target Profile (Raspberry Pi 4 Model B)
Target Images (squashfs)
```

* Under the target images tab, select squashfs. This will create a compressed read-only filesystem. This is the default option.
* Edit the Root Filesystem partition size to 7000 mb or if using a larger SD Card, 30000 MB
* Exit and save the configuration.

#### 5. Build the firmware

```bash
make -j4
```

* The -j4 option specifies the number of threads to use. This is the number of cores on your machine. If you have a 4-core machine, use -j5 to fully use all 4 cores.

#### 6. Find the firmware image you just built

```bash
cd bin/targets/bcm27xx/bcm2711
ls
```

* You should see a file named something like openwrt-bcm27xx-bcm2711-rpi-4-squashfs-factory.img.gz

#### 7. Flash the firmware image to the SD Card

* Using Raspberry Pi Imager

  * Download and install [Raspberry Pi Imager](https://www.raspberrypi.org/downloads/)
  * Insert the SD Card into your computer
  * Open Raspberry Pi Imager
  * Select the SD Card
  * Select the OpenWrt image you just built
  * Click Write

#### 8. Boot the Raspberry Pi

* Insert the SD Card into the Raspberry Pi
* Plug in your Raspberry Pi
* Connect to the Raspberry Pi using an ethernet cable
* The default IP address of the Raspberry Pi is 192.168.1.1
* Manually configure your computer's IP address to an address in the same subnet. For example, 192.168.1.2 with a subnet mask of 255.255.255.0
* Open a web browser and navigate to 192.168.1.1
* Or use SSH to connect to the Raspberry Pi

```bash
ssh root@192.168.1.1
```

* There is no password by default

## Troubleshooting

* When connecting to the Raspberry Pi using SSH, you may get a warning about the something like the following:

```bash
WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
```

* This is because the SSH key has changed. This is normal. Remove the old key from your known_hosts file and try again.

```bash
ssh-keygen -R 192.168.1.1
```

## Adding Custom Files

#### 1. Create a directory named files in the root of the OpenWrt source directory

```bash
cd source
mkdir files
```

For example, the directory structure should look like this:

```bash
source
└── files
```

#### 2. Add your custom files to the files directory

- For our case, we will add any tools that we create to the tools located inside the files folder.

```bash
cd files
mkdir tools
```

For example, the directory structure will look like this:

```bash
source
└── files
    └── tools
```
