# Raspberry Pi AP Setup Guide

This guide will walk you through the steps of installing Raspberry Pi OS, SSH into the Pi, and running the setup.sh script.

## Prerequisites

Before you begin, make sure you have the following:

- Raspberry Pi board
- MicroSD card
- Power supply
- Ethernet cable

## Step 1: Installing Raspberry Pi OS

1. Download the Raspberry Pi Imager from the [official website](https://www.raspberrypi.org/software/).
2. Open the Raspberry Pi Imager
3. Chose the Raspberry Pi 4
4. Choose Raspberry Pi OS (other)
   - Raspberry Pi OS Lite(64-bit)
5. Choose the MicroSD card
6. Click Next and then Edit Settings
7. Set the following settings:
   - Hostname: `Phoebus`
   - Username `Admin`
   - Password `password`
8. Click on the Services tab and make sure SSH is enabled
9. Boot up the Pi

## Step 2: SSH into the Pi

1. Connect the Raspberry Pi to power.
2. Connect the Raspberry Pi to your router using an Ethernet cable.
3. Wait for the Raspberry Pi to boot up.
4. Open a terminal on your computer and type the following command:
   ```bash
   ssh admin@ip_address
   ```
    Replace `ip_address` with the IP address of your Raspberry Pi.
5. Make sure the pi is connected to the internet by running the following command:
   ```bash
   ping google.com
   ```
6. If the ping is successful, you can proceed to the next step.

## Step 3: Clone the GitHub Repository

1. Install git by running the following command:
   ```bash
   sudo apt install git -y
   ```
2. Run the following command to clone the GitHub repository:
   ```bash
   git clone https://github.com/CamJak/SeniorDesign.git
    ```
3. Navigate to the APSetup directory
   ```bash
   cd SeniorDesign/APSetup/
   ```
4. Run the setup.sh script
    ```bash
    sudo bash setup.sh
    ```
    The script will setup the Pi as an access point and reboot the Pi.
