# Mountain Come To Me: Engine

The back-end side of the `mountaincometome` system.

## Installing and running

```sh
git clone https://github.com/mountaincometome/engine.git
cd engine/
. _cli/setup.sh
. _cli/start.sh
```

After that check statuses of all subsystems via `$ . _cli/status.sh`.

## Using simple CLI

* start system:

```sh
. _cli/start.sh`
```

* restart system:

```sh
. _cli/restart.sh`
```

* stop system:

```sh
. _cli/stop.sh`
```

* terminate system and `supervisor`:

```sh
. _cli/terminate.sh`
```

* view status of system:

```sh
. _cli/status.sh`
```

* install/upgrade dependencies:

```sh
. _cli/install.sh`
```

## Ports of subsystems

* 50000 -- `center`
* 50001 -- `monitor`
* 50002 -- `configurator`
* 50003 -- `pulsar`
* 50004 -- `watcher`
* 50005 -- `marker`
* 50006 -- `notifier`

## License

GPL v3
