# Alpine Linux Cloud Image Builder

(but for Scaleway)

This repository contains the scripts and configuration files to build an Alpine Linux cloud image for Scaleway. It has been forked from the [official Alpine Linux cloud image builder](https://gitlab.alpinelinux.org/alpine/cloud/alpine-cloud-images).

## Building the image

Refer to the official documentation (see README.md.orig).

## Using the image on Scaleway

First of all, download the qcow2 file from the [releases page](https://github.com/blurrycat/alpine-cloud-image-scaleway/releases) and upload it into an Object Storage bucket on your Scaleway account.

Then, import the volume into a snapshot, then create a new image from this snapshot:
```sh
scw instance snapshot create zone=fr-par-1 name=alpine-base volume-type=b_ssd bucket=<YOUR-BUCKET-NAME> key=scaleway_alpine-3.19.1-x86_64-uefi-cloudinit-r0.qcow2
scw instance image create snapshot-id=<YOUR-SNAPSHOT-ID> arch=x86_64 name=alpine-base
```

Finally, create a new instance using this snapshot:
```sh
scw instance server create type=PLAY2-PICO zone=fr-par-1 image=<YOUR-IMAGE-ID> root-volume=b:5G name=my-alpine-instance ip=new
```

You can then connect to your instance using its public IP address, and the `alpine` user. Please make sure you have at least one SSH key in your Scaleway account before creating the instance, otherwise you won't be able to connect to it.