# Systemd services rundown
i will use this doc as a place for relevant resources and to help me summarize info as i learn.

- `pwnable.service` should have the path `/etc/systemd/system/pwnable.service`
    - so this should be done in the `Dockerfile`

- service is going to run in the background, so it will *probably* need to be the `forking` type
    - `ExecStart=` script should call `fork()`

## Resources
- [debian systemd services](https://wiki.debian.org/systemd/Services)
- [systemd.service man page](https://manpages.debian.org/buster/systemd/systemd.service.5.en.html)