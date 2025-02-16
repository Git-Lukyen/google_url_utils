
# Google URL Utils

Google URL Utils is a collection of utilities designed to help you work with various Google URL components. Currently, the main focus is on decoding protocol buffer parameters embedded in Google URLs. More features (such as advanced pagination handling) may be added in the future.

## Features

- **Decode Protocol Buffer Parameters:**  
  Easily decode encoded protobuf parameters extracted from Google URLs.
- **Command-line Interface:**  
  A simple CLI tool (`decode_pb_param`) is provided for quick decoding.
- **Extensible Design:**  
  Designed to expand as more URL-related utilities are needed.

## Installation

The package is available on TestPyPI. You can install it using pip:

```bash
pip install --index-url https://test.pypi.org/simple/ google-url-utils
```

Note: This package is currently hosted on TestPyPI and is under active development.

---

## Usage

After installation, you can use the command-line tool to decode a protobuf parameter. For example:

```bash
decode_pb_param --input "<your_encoded_parameter>" [--pretty_print]
```


Important Note: Shell Behavior

If your parameter value contains exclamation marks (!), some shells (like zsh) might interpret them as history expansion commands. To prevent this behavior, disable history expansion by running:

```bash
unsetopt hist_expand
```
before running the command.

### Example

Given the command:

```bash
decode_pb_param -i "!4m12!1m3!1d500.0!2d0.0!3d0.0!2m3!1f0!2f0!3f0!3m2!1i1000!2i1000!4f13"
```


The expected output is:

[4m: [1m: [1d: 500.0, 2d: 0.0, 3d: 0.0], 2m: [1f: 0.0, 2f: 0.0, 3f: 0.0], 3m: [1i: 1000, 2i: 1000], 4f: 13.0]]

---

Author: Dracea Lucian <br>
Email: dracea.lucian.mihai@gmail.com

