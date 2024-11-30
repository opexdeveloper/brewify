Brewify
=======

.. image:: https://images-ext-1.discordapp.net/external/qG41hZHbsmNVc9WSE6aX3oVWi_LP39dQZjxZgdIdFLI/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1076140187471593492/bfea312390b3b52773f1358457d7261b.png?format=webp&quality=lossless&width=427&height=427
   :alt: Brew
   :height: 50px
   :width: 50px

Brewify is a Python library that provides a simple interface to interact with various APIs, including Google Search, IMDb, Discord, and more. It is designed to be easy to use while allowing you to extend its functionality.

Features
--------

- **API Requests**: Make GET requests to various endpoints.
- **Error Handling**: Custom exceptions for better error management.
- **Multiple Services**: Access Google Images, IMDb, Discord, and more.
- **Sentiment Analysis**: Analyze the sentiment of text.
- **Chatbot Functionality**: Engage in simple conversations.
- **Joke Generator**: Get a random joke.

Installation
------------

You can install Brewify via pip:

.. code-block:: bash

    pip install brewify

Usage
-----

**Initialize the Brewify Class**

To get started, initialize the `Brewify` class with your API key:

.. code-block:: python

    from brewify import Brewify

    brewify = Brewify(api_key="YOUR_API_KEY")

**Example Methods**

*Get Google Images*

.. code-block:: python

    image_response = brewify.get_google_image(query="cats")
    print(image_response)

*Search Google*

.. code-block:: python

    text_response = brewify.search_google(query="Python programming")
    print(text_response)

*IMDb Search*

.. code-block:: python

    imdb_response = brewify.imdb_search(query="Inception")
    print(imdb_response)

*Discord Guild Search*

.. code-block:: python

    guild_response = brewify.discord_guild_search(invite_code="your_invite_code")
    print(guild_response)

*Sentiment Analysis*

.. code-block:: python

    sentiment_response = brewify.sentiment_analysis(sentence="I love Python!")
    print(sentiment_response)

*Get a Joke*

.. code-block:: python

    joke_response = brewify.joke()
    print(joke_response)

Error Handling
--------------

Brewify raises a custom exception called `Brexception` for handling errors. You can catch it as follows:

.. code-block:: python

    try:
        brewify.some_method()
    except Brexception as e:
        print(f"An error occurred: {e}")

Contributing
------------

Contributions are welcome! Feel free to submit a pull request or open an issue.

License
-------

This project is licensed under the MIT License - see the `LICENSE` file for details.

Dependencies
-----

.. image:: https://cdn.simpleicons.org/python/cyan
   :alt: Python Icon
   :height: 50px
   :width: 50px
   :align: center
   :target: _blank

 

.. image:: https://cdn.simpleicons.org/fastapi/cyan
   :alt: FastAPI Icon
   :height: 50px
   :width: 50px
   :align: center
   :target: _blank



.. image:: https://cdn.simpleicons.org/pypi/cyan
   :alt: PyPI Icon
   :height: 50px
   :width: 50px
   :align: center
   :target: _blank

Acknowledgments
---------------

- Thanks to the developers of the APIs used in this library.
- Special thanks to `FastAPI <https://fastapi.tiangolo.com/>`_ for making API development a breeze.