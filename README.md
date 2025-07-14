# sortfqdns.py

Read FQDNs from a file, extract zone and subdomain, and print sorted unique entries.

## Usage

```
python sortfqdns.py [input_file]
```
If no `input_file` is given, defaults to `/tmp/fqdns`.

## Example

```
python sortfqdns.py myfqdns.txt
```

## Output Format

Each line of output is in the format:
```
zone:subdomain
```
If there is no subdomain, the output will be `zone:`.

## Requirements

- Python 3.x
- [tldextract](https://github.com/john-kurkowski/tldextract)
  - Install with: `apt install python3-tldextract`

## Author

Max Chudnovsky (<max@chudnovsky.ca>)

## License

MIT
