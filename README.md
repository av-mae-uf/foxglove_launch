# Foxglove Studio Launch Package

A launch package to launch foxglove studio and connect to the AV1Tenth Car. To do this, first you must install foxglove studio application using:

```
sudo snap install foxglove-studio
```

Then you can launch the package using:

```
ros2 launch foxglove_launch foxglove.launch.py
```

You will also need the foxglove layout file that we have created that you can take from the layout folder in the repo. You can import this by going into the layouts tab on foxglove.
