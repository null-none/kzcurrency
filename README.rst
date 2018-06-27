=======
Install
=======

.. code-block:: bash

    pip install kz-currency


=======
Example
=======

.. code-block:: python

    from kzcurrency.list import KZCurrency

    currency = KZCurrency()
    print(currency.list())
    print(currency.rates())
    print(currency.get('USD'))


=======
License
=======

MIT
