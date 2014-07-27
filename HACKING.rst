i18n
---------------

- using lingua, extract messages.
- using msginit,msgupdate modify catalogs.
  should I use pybabel for this phase?
- using babel, compile catalogs.

::

  $ pot-create rebecca -o rebecca/bootstraplayout/locale/rebecca.bootstrap.pot

::

  $ cd rebecca/bootstraplayout/local
  $ mkdir -p ja/LC_MESSAGES
  $ msginit -l ja -o ja/LC_MESSAGES/rebecca.bootstraplayout.po

::

  $ pybabel compile -D rebecca.bootstraplayout -l ja -d rebecca/bootstraplayout/local


