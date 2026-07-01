# TrueNAS Homelab

A personal homelab built to learn storage, virtualization, networking, and remote administration using **TrueNAS Scale**.

## Overview

This repository documents my TrueNAS homelab setup and the projects running on it. I use it as a learning environment to practice:

* Storage management
* Virtualization
* Network configuration
* User and permission management
* Remote access
* System troubleshooting and documentation

## Hardware

* **Host:** Acer Nitro AN515-55 laptop
* **CPU:** Intel Core i5-10300H
* **Memory:** 47 GiB RAM available to TrueNAS
* **Boot Drive:** 512 GB NVMe SSD
* **Storage Pool:** `tank`
* **Available Storage:** 4.22 TiB

## Network Layout

* **LAN:** `192.168.1.0/24`
* **Router:** `192.168.1.1`
* **TrueNAS Server:** `192.168.1.20`
* **Pi-hole:** `192.168.1.10`
* **VM Network:** Static IPs on the local LAN

## What’s Running on TrueNAS

### Virtual Machines

| VM            |     IP Address | Purpose                                  |
| ------------- | -------------: | ---------------------------------------- |
| Ubuntu Server | `192.168.1.30` | General Linux server, apps, and lab work |
| Windows 11    | `192.168.1.32` | Windows management and testing           |
| Kali Linux    | `192.168.1.33` | Security tools and network testing       |

> Note: My **macOS VM is not hosted on TrueNAS**. It runs on **VMware Workstation Pro** on my personal laptop.

### Network Services

* **Pi-hole** for DNS filtering and ad blocking
* Remote access for management and administration
* File storage and dataset organization
* Snapshot-based recovery planning

## Goals of the Lab

* Learn how to manage storage and datasets in TrueNAS
* Practice virtualization and VM provisioning
* Build a secure and reliable home network
* Document troubleshooting steps and lessons learned
* Create portfolio material for GitHub and job applications

## Features

* Centralized storage on a ZFS pool
* VM hosting for Linux, Windows, and security testing
* Local DNS filtering with Pi-hole
* Basic network segmentation and access control
* Manual documentation for recovery and future expansion

## Screenshots

Add screenshots here as the project grows.

```text
/images/truenas-dashboard.png
/images/storage-pool.png
/images/vm-list.png
/images/network-diagram.png
```

## Project Structure

```text
truenas-homelab/
├── README.md
├── images/
├── diagrams/
├── docs/
├── vms/
└── scripts/
```

## Lessons Learned

* Planning storage early makes the setup easier to manage later.
* Clear documentation helps when rebuilding or troubleshooting.
* Static IP assignments make lab services easier to track.
* Virtual machines are useful for testing without affecting the main system.

## Future Improvements

* Add more detailed network diagrams
* Expand backup and snapshot documentation
* Document VM provisioning steps
* Add scripts for maintenance tasks
* Improve security and access controls

## Why I Built This

This lab gives me a real environment to practice skills that matter in IT and cybersecurity, including storage management, virtualization, networking, and troubleshooting. It also serves as a portfolio project that shows how I organize and support a working homelab.

## License

This project is for personal learning and portfolio use.
