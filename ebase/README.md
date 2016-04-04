ebase
=====================

Developer Notes
---------------------
static javascript is compiled from

    ebase/<app_name>/static/<app_name>/coffee
to

    ebase/<app_name>/static/<app_name>/lib
and all js files are referenced by their same name with a js extension. The coffee watcher is helpful here: 

    coffee -o lib -cw coffee
