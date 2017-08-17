# Mountain Come To Me

The `mountaincometome` system.

## Installing and running

```
$ git clone https://github.com/signaldetect/mountaincometome.git
$ cd mountaincometome/
$ . _cli/setup.sh
$ . _cli/start.sh
```

After that check statuses of all subsystems via `$ . _cli/status.sh`.

## Using simple CLI

* start system:

`$ . _cli/start.sh`

* restart system:

`$ . _cli/restart.sh`

* stop system:

`$ . _cli/stop.sh`

* terminate system and `supervisor`:

`$ . _cli/terminate.sh`

* view status of system:

`$ . _cli/status.sh`

* install/upgrade dependencies:

`$ . _cli/install.sh`

## Ports of subsystems

* 50000 -- `center`
* 50001 -- `monitor`
* 50002 -- `configurator`
* 50003 -- `pulsar`
* 50004 -- `watcher`
* 50005 -- `marker`
* 50006 -- `notifier`
