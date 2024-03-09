# auto-dotenv

`auto-dotenv` is a python package that simplifies the process of loading environment variables from a `.env`
file in your project. With `auto-dotenv`, you no longer need to manually load the `.env` file in your code.
This package automatically loads the variables from the `.env` file if the `auto-dotenv` package is installed
in your environment.

`auto-dotenv` is just a wrapper around `python-dotenv`. In fact what it does is basically run the following code everytime you run a python file:

```python
from dotenv import load_dotenv

load_dotenv()
```

### Installation

You can install `auto-dotenv` via pip:

```bash
pip install auto-dotenv
```

### Usage

Using `auto-dotenv` is straightforward. Once you've installed the package, that's it!
If a `.env` file is present in your project directory,
`auto-dotenv` will automatically load its contents into the environment.

You can define the following environment variable to override the default .env file: `AUTO_DOTENV_PATH`, `AUTO_DOTENV_ENV`

### Example

Let's say you have a `.env` file with the following contents:

```
DB_HOST=localhost
DB_USER=admin
DB_PASS=password123
```

Normally, you would need to load these variables manually in your code. However, with `auto-dotenv`, you can access these variables directly from the environment:

```python
import os

print(os.environ['DB_HOST'])  # Output: localhost
print(os.environ['DB_USER'])  # Output: admin
print(os.environ['DB_PASS'])  # Output: password123
```

### Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on [GitHub](https://github.com/hmiladhia/auto-dotenv).

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Disclaimer

This package comes with no warranties or guarantees. Use it at your own risk.
